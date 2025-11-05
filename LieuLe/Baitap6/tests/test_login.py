import json
import os
from pages.login_page import LoginPage
from playwright.async_api import expect
from playwright.sync_api import sync_playwright
import time

def test_login_successfully(page):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        login_page = LoginPage(page)
        login_page._take_screenshot("login_error")
        login_page.loginwith("standard_user", "secret_sauce")
        time.sleep(5)   
        screenshot_path = os.path.join("screenshots", "login_result.pnj")
        login_page._take_screenshot(screenshot_path)
        assert "dashboard" in page.url.lower(), "Login failed!"

        browser.close()
        if __name__ == "__main__":
            test_login_successfully()
