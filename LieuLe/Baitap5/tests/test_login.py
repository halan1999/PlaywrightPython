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
        print("Login successfully!")
        time.sleep(5)
        browser.close()

def test_login_unsuccessfully():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  
        page = browser.new_page()
        login_page = LoginPage(page)
        login_page.goto()
        login_page.loginwith("standard_user", "123456")
        expect(login_page.get_error_message()).to_have_text("Epic sadface: Username and password do not match any user in this service")
        time.sleep(5)
        browser.close()