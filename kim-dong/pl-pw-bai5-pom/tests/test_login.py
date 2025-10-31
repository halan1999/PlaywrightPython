import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from playwright.sync_api import sync_playwright

from pages.login_page import LoginPage
from playwright.sync_api import expect

def test_successful_login_standard_user():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        login_page = LoginPage(page)

        login_page = LoginPage(page)
        login_page.login("standard_user", "secret_sauce")
        login_page.assert_login_successful()

def test_login_failure_locked_user():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        login_page = LoginPage(page)
        
        login_page = LoginPage(page)
        login_page.login("locked_out_user", "secret_sauce")

        expected_message = "Epic sadface: Sorry, this user has been locked out."
        login_page.assert_error_message_visible(expected_message)

if __name__ == "__main__":
    test_successful_login_standard_user()
    test_login_failure_locked_user()