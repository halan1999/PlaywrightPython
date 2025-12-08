import pytest
from playwright.sync_api import Playwright
from pages.login_page import LoginPage

@pytest.fixture
def login_page(page):
    return LoginPage(page)
