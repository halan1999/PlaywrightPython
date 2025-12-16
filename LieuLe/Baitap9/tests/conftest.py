import pytest
from playwright.sync_api import Playwright
from pages.dashboard_page import DashboardPage
from pages.login_page import LoginPage

#1. Page object : LoginPage
@pytest.fixture
def login_page(page):
    return LoginPage(page)

#2. Login page with fixture 
@pytest.fixture
def login_in_page (login_page: LoginPage):
    login_page.open()
    login_page.login_valid_user()
    
    return login_page

@pytest.fixture
def logged_in_page(login_page):
    login_page.login_valid_user()
    return login_page.page

@pytest.fixture
def dashboard_page(page):
    return DashboardPage(page)
