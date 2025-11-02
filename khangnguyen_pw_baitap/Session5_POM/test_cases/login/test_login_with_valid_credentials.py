from playwright.sync_api import Page
from pages.login_page import LoginPage
from pages.home_page import HomePage
from test_data.credentials_loader import get_valid

def test_login_with_valid_credentials(page: Page):
    # Get invalid credentials from JSON file
    username, password = get_valid() 

    # Create an object from LoginPage class
    login_page = LoginPage(page)
    
    # Open URL of login page
    login_page.open()

    # Login with valid credentials
    login_page.login(username, password)

    # Test expected: username 'admin_example' is visible
    # Create an object from HomePage class
    home_page = HomePage(page) 
    assert home_page.is_loaded()
