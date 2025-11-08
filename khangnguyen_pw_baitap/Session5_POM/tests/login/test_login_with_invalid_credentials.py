from playwright.sync_api import Page
from pages.login_page import LoginPage
import json
from pathlib import Path

def test_login_with_invalid_credentials(page: Page):
    # Get invalid credentials from JSON file
    path = Path("resources/login_credentials.json")
    with path.open("r", encoding="utf-8") as file:
        credentials = json.load(file)

    valid_user = credentials["invalid"]
    username = valid_user["username"]
    password = valid_user["password"]

    login_page = LoginPage(page) 

    # Open login page
    login_page.open()
    login_page.take_screenshot("login_page.png")

    # Login
    login_page.login(username, password)

    # Test expected: toast message is visible
    assert login_page.is_invalid_toast_visible()
    login_page.take_screenshot("login_page_with_toast_error_message.png")
