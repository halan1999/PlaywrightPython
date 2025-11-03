from pages.login_page import LoginPage
from playwright.sync_api import expect, Page
import time
import json

with open(file= r"./data/credentials.json", mode="r", encoding="utf-8") as file:
    data = json.load(file)
    login_account = data["saucedemo"]

def test_login_successfully(page):
    login_page = LoginPage(page)
    # login_page.goto()
    login_page.login(login_account["username"],login_account["password"])
    print("Login successfully")
    
def test_login_failed_empty_username_password(page: Page):
    login_page = LoginPage(page)
    # login_page.goto()
    login_page.login("","")
    print("Login failed")

def test_login_failed_invalid_username(page: Page):
    login_page = LoginPage(page)
    # login_page.goto()
    login_page.login("admin","123456")
    print("Login failed due to invalid username")

def test_login_failed_invalid_password(page: Page):
    login_page = LoginPage(page)
    # login_page.goto()
    login_page.login("admin_example","123457")
    print("Login failed due to invalid password")
    
    
