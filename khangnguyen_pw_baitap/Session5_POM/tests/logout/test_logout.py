from pages.login_page import LoginPage
from pages.home_page import HomePage
from components.header_component import HeaderComponent
from playwright.sync_api import Page, expect
import json
from pathlib import Path

def test_logout_functionality(page):
    login_page = LoginPage(page)
    home_page = HomePage(page)
    header = HeaderComponent(page)

    # Open login page
    login_page.open()
    login_page.take_screenshot("login_page.png")

    # Login
    login_page.login_valid()

    # Expected: Home page is loaded
    assert home_page.is_loaded()
    home_page.take_screenshot("home_page.png")

    # Log out
    header._logout()
    assert login_page.is_loaded()

