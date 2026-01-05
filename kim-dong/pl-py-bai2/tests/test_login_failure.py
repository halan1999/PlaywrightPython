import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage

def test_login_failure():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        login_page = LoginPage(page)

        login_page.navigate()
        login_page.login("standard_user", "sai_mat_khau")
        print("Kiểm tra message khi đăng nhập sai")

        expected_message = "Epic sadface: Username and password do not match any user in this service"
        login_page.verify_login_failure(expected_message)

        browser.close()

if __name__ == "__main__":
    test_login_failure()
