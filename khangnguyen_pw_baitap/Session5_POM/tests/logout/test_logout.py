from pages.login_page import LoginPage
from pages.home_page import HomePage
from components.header_component import HeaderComponent
from playwright.sync_api import Page, expect
import json
from pathlib import Path

def test_logout_functionality(page):
    ## Get valid credentials from JSON file
    path = Path("resources/login_credentials.json")
    with path.open("r", encoding="utf-8") as file:
        credentials = json.load(file)

    valid_user = credentials["valid"]
    username = valid_user["username"]
    password = valid_user["password"]

    login_page = LoginPage(page)
    home_page = HomePage(page)
    header = HeaderComponent(page)

    # Open login page
    login_page.open()
    login_page.take_screenshot("login_page.png")

    # Login
    login_page.login(username, password)

    # Expected: Home page is loaded
    assert home_page.is_loaded()
    home_page.take_screenshot("home_page.png")

    # Log out
    header._logout()
    assert login_page.is_loaded()

