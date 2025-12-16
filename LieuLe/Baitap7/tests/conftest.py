import pytest
from pages.dashboard_page import DashboardPage
from pages.login_page import LoginPage

@pytest.fixture
def login_page(page):
    return LoginPage(page)


@pytest.fixture
def logged_in_page(page):
    login = LoginPage(page)
    login.open()
    login.login_valid_user()   
    page.wait_for_url("**/erp/desk") 
    return page


@pytest.fixture
def dashboard(logged_in_page):
    return DashboardPage(logged_in_page)
