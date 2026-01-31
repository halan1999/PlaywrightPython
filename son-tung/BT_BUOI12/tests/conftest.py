import pytest

from BT_BUOI12.pages.multitabs.orangehrm_page import OrangePage
from BT_BUOI12.pages.login.login_page import LoginPage
from playwright.sync_api import Page

@pytest.fixture
def login_page(page):
    return LoginPage(page)

@pytest.fixture
def logged_in_page(login_page):
    login_page.goto()
    login_page.login_user("valid_user")
    return login_page

@pytest.fixture(scope="class")
def logged_in_class(request, browser):
    context = browser.new_context()
    page = context.new_page()

    # Login 1 lần cho cả class
    lp = LoginPage(page)
    lp.goto()
    lp.login_user("valid_user")
    lp.header.wait_for_user_logged_in()

    request.cls.page = page
    request.cls.login_page = lp
    request.cls.context = context

    yield

    context.close()

@pytest.fixture
def windows_page(page: Page) ->OrangePage:
    wp = OrangePage(page)
    wp.open_url()
    return wp