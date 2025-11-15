import json
import os
from ..pages.login_page import LoginPage
from playwright.sync_api import sync_playwright
import time
#from ..utils.load_data import load_user_from_json

def test_login_successfully():
     with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        
        login_page = LoginPage(page, "LieuLe/Baitap6/data/credentials.json")
        login_page._take_screenshot("before_login.jpeg")
        username, password = login_page.load_credentials("valid")
        login_page._take_screenshot("after_login.jpeg")
        login_page.loginwith()
        login_page.verify_login_success()

        browser.close() 
def test_login_unsuccessfully():
     with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        login_page = LoginPage(page, "LieuLe/Baitap6/data/credentials.json")
        login_page.loginwith("invalid")

        error_text = login_page.get_error_message()
        print("Toast mesage:", error_text)
        expected_message = "Invalid Login Credentials." 
        assert expected_message in error_text, f"Expected '{expected_message}', but got '{error_text}'"
        browser.close() 
        