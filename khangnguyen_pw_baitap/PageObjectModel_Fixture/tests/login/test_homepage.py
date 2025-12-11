from pages.login_page import LoginPage
from pages.home_page import HomePage
from components.header_component import HeaderComponent

def test_project_menu_visible(logged_in_page):
    home_page = HomePage(logged_in_page)
    assert home_page.is_project_menu_visible()