

import pytest
from playwright.sync_api import Playwright
from pages.login_page import LoginPage

# 1. Page Object: LoginPage
@pytest.fixture
def login_page(page):
    return LoginPage(page)

# 2. Fixture thực hiện login (optional nếu cần login sẵn)

@pytest.fixture
def open_login_page(page,login_page):
    login_page.open()
    return page   


@pytest.fixture
def logged_in_page(login_page):
    login_page.open()
    login_page.login_valid_user()
    return login_page   


# Class scope
@pytest.fixture(scope="class")
def logged_in_class(request, browser):
    context = browser.new_context()
    page = context.new_page()

    # Login 1 lần cho cả class
    lp = LoginPage(page)
    lp.open()
    lp.login_valid_user()
    # lp.header.wait_for_user_logged_in()

    # Gán vào class
    request.cls.page = page
    request.cls.login_page = lp
    request.cls.context = context

    yield 

    # Teardown khi class chạy xong
    context.close()

# Module scope
@pytest.fixture(scope="module")
def logged_in_module(browser):
    context = browser.new_context()
    page = context.new_page()

    lp = LoginPage(page)
    lp.open()
    lp.login()
    lp.header.wait_for_user_logged_in()

    yield page, lp

    # logout khi module chạy xong
    lp.logout()
    context.close()
