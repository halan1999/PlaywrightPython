import pytest
from playwright.sync_api import Playwright, Page
from pages.login_base import LoginPage

# 1. Page Object: LoginPage
@pytest.fixture
def login_page(page):
    return LoginPage(page)

# 2. Fixture thực hiện open page LoginPage
@pytest.fixture
def navigave(page,login_page):
    login_page.open_login_page()
    return page

# 3. Fixture thực hiện login 1 lần cho cả class
@pytest.fixture
def logged_in_class(request, browser):
    context = browser.new_context()
    page = context.new_page()

    lp = LoginPage(page)
    lp.open_login_page()
    lp.valid_user()
    # Gán vào class
    request.cls.page = page
    request.cls.login_page = lp
    request.cls.context = context

    yield
    # Teardown khi class chạy xong
    context.close()