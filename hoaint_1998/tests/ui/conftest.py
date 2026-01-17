from pages.HRM.Login.login_page import LoginPage
from pages.HRM.home.home_page import HomePage
import pytest
from utils.json_loader import load_json_file
import os
import random
import string
from faker import Faker


file_path_json_login_data = os.path.join(os.getcwd(), "data", "login_data", "credentials.json")

cred = load_json_file(file_path_json_login_data)
valid_user = cred["valid_user"]
base_url = "https://hrm.anhtester.com/erp"

@pytest.fixture
def login_page(page) -> LoginPage:
    return LoginPage(page)

@pytest.fixture
def logined_page(login_page) -> LoginPage:
    login_page.go_to_login_page(base_url)
    login_page.login(valid_user["username"], valid_user["password"])
    login_page.verify_login_success()
    return login_page

@pytest.fixture
def home_page(page, logined_page) -> HomePage:
    home = HomePage(page)
    home._verify_home_page()
    return home

@pytest.fixture(scope="session")
def api_context_antester(playwright):
    request_context = playwright.request.new_context(
        base_url="https://book.anhtester.com",
        extra_http_headers={
            "Accept": "application/json"
        }
    )
    yield request_context
    request_context.dispose()

@pytest.fixture
def new_user_data():
    faker = Faker()
    return {
        "email": faker.email(),
        "name": faker.name_female(),
        "password": "HoaiNT",
        "phone": faker.phone_number(),
        "address": faker.address(),
        "avatarUrl": ""
    }