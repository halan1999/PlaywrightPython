from playwright.sync_api import Page
from pages.login_page import LoginPage
from resources.credentials_loader import get_invalid

def test_login_with_invalid_credentials(page: Page):
    # Get invalid credentials from JSON file
    username, password = get_invalid() 

    login_page = LoginPage(page) 

    # Open login page
    login_page.open()
    # Take a screenshot of login page
    login_page.take_screenshot("login_page.png")

    # Login
    login_page.login(username, password)

    # Test expected: toast message is visible
    assert login_page.is_invalid_toast_visible()
    login_page.take_screenshot("login_page_with_toast_error_message.png")
