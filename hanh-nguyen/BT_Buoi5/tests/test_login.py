from pages.login_page import LoginPage
from playwright.sync_api import expect
# import json
# from pages.login_page import LoginPage

# def test_login_from_json(page):
#     login_page = LoginPage(page)

#     with open("BT_Buoi5\data\credentials.json") as f:
#         creds = json.load(f)

#     valid = creds["valid_user"]

#     login_page.login(valid["username"], valid["password"])
#     login_page.assert_login_successful()


def test_login_succeeded_standard_user(page):
    login_page = LoginPage(page)
    login_page.login("standard_user", "secret_sauce")
    login_page.assert_successfully_login()

def test_login_failed_locked_user(page):
    login_page = LoginPage(page)
    login_page.login("locked_out_user", "secret_sauce")
    login_page.assert_error_message_visible("Epic sadface: Sorry, this user has been locked out.")

def test_login_blank_username(page):
    login_page = LoginPage(page)
    login_page.login("", "secret_sauce")
    login_page.assert_error_message_visible("Epic sadface: Username is required")

def test_login_blank_username(page):
    login_page = LoginPage(page)
    login_page.login("visual_user", "")
    login_page.assert_error_message_visible("Epic sadface: Password is required")

def test_login_blank_both(page):
    login_page = LoginPage(page)
    login_page.login("", "")
    login_page.assert_error_message_visible("Epic sadface: Password is required")

def test_login_incorrect_username(page):
    login_page = LoginPage(page)
    login_page.login("123456", "secret_sauce")
    login_page.assert_error_message_visible("Epic sadface: Username and password do not match any user in this service")

def test_login_incorrect_password(page):
    login_page = LoginPage(page)
    login_page.login("performance_glitch_user", "123456")
    login_page.assert_error_message_visible("Epic sadface: Username and password do not match any user in this service")

def test_login_incorrect_both(page):
    login_page = LoginPage(page)
    login_page.login("123456", "123456")
    login_page.assert_error_message_visible("Epic sadface: Username and password do not match any user in this service")