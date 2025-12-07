import pytest
from playwright.sync_api import Playwright
from pages.login_page import LoginPage


#1. Page Object: Login Page
@pytest.fixture
def login_page(page):
    return LoginPage(page)


#2. Fixture thực hiện login (optional nếu cần login sẵn)
@pytest.fixture
def logged_in_page(page):
    login = LoginPage(page)
    login.login_valid_user()
    # login_page.header.wait_for_user_logged_in()
    return page

@pytest.fixture
def set_up_data(logged_in_page):
    pass

#3. Class scope
# @pytest.fixture(scope="class")
# def logged_in_class(request, browser):
#     context = browser.new_context()
#     page = context.new_page()

#     #Login 1 lần cho cả class
#     lp = LoginPage(page)
#     lp.open()
#     lp.login()
#     lp.header.wait_for_user_logged_in()
