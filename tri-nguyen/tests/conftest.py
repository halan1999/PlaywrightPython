from playwright.sync_api import Playwright
from pages.login_page import LoginPage
import pytest

# 1. Page Opject: Login Page
@pytest.fixture
def login_page(page):
    return LoginPage(page)

# 2. Login Page perform login
@pytest.fixture
def perform_login(login_page):
    login_page.login_withUsernamePassword()
    return login_page

