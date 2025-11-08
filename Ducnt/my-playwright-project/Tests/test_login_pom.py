
from pages.login_page import LoginPage
import json
from playwright.sync_api import Page

def test_login_with_valid_credentials(page: Page):
    login_page = LoginPage(page)
    
    with open("/Users/ducnt/PlaywrightPython/Ducnt/my-playwright-project/data/scredentials.json") as f:
        creds = json.load(f)

    valid = creds["valid_user"]
    login_page.login(valid["username"], valid["password"])
    login_page.assert_login_successful()
    login_page.logout()
    login_page.assert_logout_successful()
    




















# from pages.login_page import LoginPage
# from playwright.sync_api import expect

# def test_successful_login_standard_user(page):
#     login_page = LoginPage(page)
#     login_page.login("standard_user", "secret_sauce")
#     login_page.assert_login_successful()

# def test_login_failure_locked_user(page):
#     login_page = LoginPage(page)
#     login_page.login("locked_out_user", "secret_sauce")
#     login_page.assert_error_message_visible("Epic sadface: Sorry, this user has been locked out.")