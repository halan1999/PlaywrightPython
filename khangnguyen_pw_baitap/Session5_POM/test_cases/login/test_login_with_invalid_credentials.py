from playwright.sync_api import Page
from pages.login_page import LoginPage
from test_data.credentials_loader import get_invalid

def test_login_with_invalid_credentials(page: Page):
    # Get invalid credentials from JSON file
    username, password = get_invalid() 

    # Create an object from LoginPage class
    login_page = LoginPage(page) 
    
    # Open URL of login page
    login_page.open()

    # Login with invalid credentials
    login_page.login(username, password)

    # Test expected: toast message is visible
    assert login_page.is_invalid_toast_visible()
