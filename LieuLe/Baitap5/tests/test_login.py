from ..pages.login_page import LoginPage
from playwright.sync_api import sync_playwright, expect
import time

def test_login_successfully():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # <--- chỉ cần đổi đây
        page = browser.new_page()
        login_page = LoginPage(page)
        login_page.goto()
        login_page.loginwith("standard_user", "secret_sauce")
        expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
        time.sleep(5)
        browser.close()