from pages.login_page import LoginPage
from playwright.sync_api import expect, Page, sync_playwright
import time
import json

def test_login_successfully(loggedinPage):
    loggedinPage.run_header_flow()
    print("Login successfully")

def test_login_failed_invalid_user(loginPage):
    loginPage.login_with_invalid_user()
    print("Login failed due to invalid credetials")
    
def test_login_failed_empty_credential(loginPage):
    loginPage.login_with_empty_credential()
    print("Login failed due to invalid credetials")


    
