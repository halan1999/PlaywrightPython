import pytest
from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage

@pytest.fixture
def loginPage(page):
    loginPage = LoginPage(page)
    loginPage.goto()
    return loginPage

@pytest.fixture
def loggedinPage(loginPage):
    loginPage.login_with_valid_user()
    yield loginPage

@pytest.fixture(scope="class")
def logged_in_class(request, browser):
    context = browser.new_context()
    page = context.new_page()

    loginPage = LoginPage(page)
    loginPage.goto()
    login_with_valid_user("hrm_user")

    # Gán vào class
    request.cls.page = page
    request.cls.loginPage = loginPage
    request.cls.context = context

    yield
    
    context.close()
