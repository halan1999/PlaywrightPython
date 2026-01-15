from pages.login_base import LoginPage
from playwright.sync_api import Playwright
import pytest

@pytest.mark.usefixtures("navigave")
def test_login_success(login_page):
    login_page.valid_user()

@pytest.mark.usefixtures("navigave")
def test_login_invalid_user(login_page):
    login_page.invalid_user()

@pytest.mark.usefixtures("navigave")
def test_login_blank_user(login_page):
    login_page.blank_user()
