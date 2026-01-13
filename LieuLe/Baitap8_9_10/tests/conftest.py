import pytest
from playwright.sync_api import Playwright
from LieuLe.Baitap8_9_10.pages.login.login_page import LoginPage

@pytest.fixture
def login_page(page):
    return LoginPage(page)

@pytest.fixture
def login_in_page(login_page):
    login_page.open()
    login_page.login_valid_user()
    return login_page

