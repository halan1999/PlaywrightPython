import pytest
from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage
from pages.social_page import SocialPage
from pages.dashboard_page import DashboardPage

@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        yield browser
        browser.close()

@pytest.fixture()
def context(browser):
    ctx = browser.new_context()
    yield ctx
    ctx.close()

@pytest.fixture()
def page(context):
    p = context.new_page()
    yield p
    p.close()

@pytest.fixture()
def login(page):
    login_page = LoginPage(page)
    login_page.load()
    return login_page

@pytest.fixture()
def social_page():
    def create(page):
        return SocialPage(page)
    return create

@pytest.fixture()
def dashboard_page():
    def create(page):
        return DashboardPage(page)
    return create
