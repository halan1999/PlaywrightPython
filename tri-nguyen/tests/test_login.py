from pages.login_page import LoginPage
from playwright.sync_api import expect
import json

def test_login_successfully(page):
    # open login page
        login_page = LoginPage(page)
        login_page.goto()
    # login by username / password
        login_page.login_withUsernamePassword()