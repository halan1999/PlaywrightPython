from pages.login_page import LoginPage
from pages.home_page import HomePage
from components.header_component import HeaderComponent

def test_project_menu_visible(logged_in_page):
    home_page = HomePage(logged_in_page)
    assert home_page.is_project_menu_visible()

def test_logout_button_visible(logged_in_page):
    home_page = HomePage(logged_in_page)
    assert home_page.is_logout_button_visible()

def test_click_header_menu_and_screenshot(logged_in_page):
    header = HeaderComponent(logged_in_page)
    header.click_header_icons()