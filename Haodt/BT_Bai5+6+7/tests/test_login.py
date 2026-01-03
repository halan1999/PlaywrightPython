from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage

def test_login_flow(login_page):
    login_page.open()
    login_page.login_valid_user()
    # login_page.run_header_flow()
    # login_page.run_menu()

def test_logout(login_page):
    login_page.open()
    login_page.login_valid_user()
    login_page.logout()

        
