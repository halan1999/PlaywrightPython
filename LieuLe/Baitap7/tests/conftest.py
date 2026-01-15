import pytest
from playwright.sync_api import expect
from pages.dashboard_page import DashboardPage
from pages.login_page import LoginPage
from utils.config import DESK_URL
from components.left_menu.left_menu_component import LeftMenuComponent

@pytest.fixture
def login_page(page):
    return LoginPage(page)


@pytest.fixture
def logged_in_page(page):
    login = LoginPage(page)
    login.open()
    login.login_valid_user()   
    expect(page).to_have_url(DESK_URL) 
    return page


@pytest.fixture
def dashboard(logged_in_page):
    return DashboardPage(logged_in_page)

@pytest.fixture
def left_menu_component(logged_in_page):
    return LeftMenuComponent(logged_in_page)