from playwright.sync_api import Page
from pages.HRM.login_page import LoginPage

def test_login_success(login_page):
    login_page.open()
    login_page.login("admin_example", "123456")
    login_page.assert_login_success()