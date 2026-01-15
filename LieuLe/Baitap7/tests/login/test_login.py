from playwright.sync_api import Playwright
from pages.login_page import LoginPage

def test_login(login_page):
    login_page.login_valid_user()
    login_page.verify_login_success()
    

