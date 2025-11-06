from pages.login_page import LoginPage
from pages.home_page import HomePage
from resources.credentials_loader import get_valid
from components.header_components import HeaderComponent
from playwright.sync_api import Page, expect

def test_logout_functionality(page):
    # Get invalid credentials from JSON file
    username, password = get_valid()

    login_page = LoginPage(page)
    home_page = HomePage(page)
    header_component = HeaderComponent(page)

    # Open login page
    login_page.open()
    # Take a screenshot of login page
    login_page.take_screenshot("login_page.png")

    # Login
    login_page.login(username, password)

    # Expected: Home page is loaded
    assert home_page.is_loaded()
    # Take a screenshot of home page
    home_page.take_screenshot("home_page.png")

    # Log out
    header_component._logout()
    assert login_page.is_loaded()

