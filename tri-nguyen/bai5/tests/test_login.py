from pages.login_page import LoginPage
from playwright.sync_api import expect

def test_login_successfully(page):
    login_page = LoginPage(page)
    login_page.goto()
    login_page.login_withUsernamePassword("admin_example","123456")