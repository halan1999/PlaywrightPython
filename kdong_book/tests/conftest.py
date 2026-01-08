import pytest
import random
import string
from playwright.sync_api import Playwright, sync_playwright
from config.env_config import EnvConfig
from models.user_model import *
from core.api_client import APIClient

def random_email():
    suffix = "".join(random.choices(string.ascii_lowercase + string.digits, k=8))
    return f"kimqa_{suffix}@mailinator.com"

def random_password():
    return "Test@123456"  # demo; có thể đổi theo rule của hệ thống

@pytest.fixture
def new_user_data():
    return {
        "email": random_email(),
        "name": "KiDo",
        "password": random_password(),
        "phone": "0900000000",
        "address": "HCM",
        "avatarUrl": ""
    }

@pytest.fixture(scope="session")
def playwright():
    pw = sync_playwright().start()
    yield pw
    pw.stop()

@pytest.fixture(scope="session")
def api_context(playwright: Playwright):
    request = playwright.request.new_context(
        base_url=EnvConfig.API_BASE_URL,
        extra_http_headers={
            "Accept": "application/json",
            "Content-Type": "application/json",
        },
        timeout=30_000,
    )
    yield request

    request.dispose()

class UserObject:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

@pytest.fixture
def register_user(playwright, new_user_data):
    """Fixture thực hiện đăng ký user mới"""
    api_context = playwright.request.new_context(base_url=EnvConfig.API_BASE_URL)
    response = api_context.post("/api/register", data=new_user_data)
    assert response.status == 201
    yield new_user_data
    api_context.dispose()

@pytest.fixture
def auth_token(api_context, register_user):
    """Fixture login và lấy access token"""
    payload = {
        "email": register_user["email"],
        "password": register_user["password"]
    }
    response = api_context.post("/api/login", data=payload)
    assert response.status == 200
    return response.json().get("accessToken")

@pytest.fixture
def auth_api_client(api_context, auth_token):
    headers = {
        "Authorization": f"Bearer {auth_token}",
        "Content-Type": "application/json"
    }
    # Khởi tạo context mới với headers cố định
    context = playwright.request.new_context(
        base_url=EnvConfig.API_BASE_URL,
        extra_http_headers=headers
    )
    yield context
    context.dispose()
@pytest.fixture(scope="session")
def browser_context(playwright: Playwright):
    """
    Browser context dùng chung cho UI tests
    """
    browser = playwright.chromium.launch(headless=False)

    context = browser.new_context(
        base_url=EnvConfig.UI_BASE_URL,
        viewport={"width": 1440, "height": 900},
    )

    yield context

    context.close()
    browser.close()


@pytest.fixture
def page(browser_context):
    """
    Page mới cho mỗi test UI (isolated)
    """
    page = browser_context.new_page()
    yield page
    page.close()