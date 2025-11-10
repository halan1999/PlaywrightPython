from pages.login_page import LoginPage
from playwright.sync_api import expect, Page, sync_playwright
import time
import json

def test_login_successfully(loggedPage):
    loggedPage.run_header_flow()
    print("Login successfully")

def test_login_failed_invalid_user(loginPage):
    loginPage.login_with_invalid_user()
    print("Login failed due to invalid credetials")
    
# def test_login_failed_empty_username_password(page: Page):
#     login_page = LoginPage(page)
#     # login_page.goto()
#     login_page.login("","")
#     print("Login failed")

# def test_login_failed_invalid_username(page: Page):
#     login_page = LoginPage(page)
#     # login_page.goto()
#     login_page.login("admin","123456")
#     print("Login failed due to invalid username")

# def test_login_failed_invalid_password(page: Page):
#     login_page = LoginPage(page)
#     # login_page.goto()
#     login_page.login("admin_example","123457")
#     print("Login failed due to invalid password")
    
    
