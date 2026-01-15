from pages.login_page import LoginPage
from pages.home_page import HomePage
from components.header_component import HeaderComponent
import json
from pathlib import Path

def test_login_with_valid_credentials(page):
    # Get valid credentials from JSON file
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
    login_page.take_screenshot("input_credentials.png")


    # Expected: Home page is loaded
    assert home_page.is_loaded()
    # Take a screenshot of home page
    home_page.take_screenshot("home_page.png")

    # Click each header icons
    header.click_header_icons()



