from pages.login_page import LoginPage
from components.header_components import HeaderComponents
from components.menu_bar_components import MenuBarComponents
from playwright.sync_api import Page
import pytest
import json

base_url = "https://hrm.anhtester.com/erp"
username = "admin_example"
password = "123456"

with open("data/credentials.json") as f:
        creds = json.load(f)

@pytest.mark.skip(reason="None")
def test_case_1(page):
    """
    1. di chuyển đến màn login
    2. thực hiện đăng nhập account hợp lệ
    3. verify login
    """
    login_page = LoginPage(page)
    login_page.go_to_login_page(base_url)
    login_page.login(username, password)
    login_page.verify_login_success()

@pytest.mark.skip(reason="None")
def test_case_2(page):
    """
    1. di chuyển đến màn login
    2. thực hiện đăng nhập account ko hợp lệ
    3. verify login
    """
    login_page = LoginPage(page)
    login_page.go_to_login_page(base_url)
    login_page.login("hoaint4398@gmail.com", password)
    login_page.verify_login_failure_invalid_credentials()

@pytest.mark.skip(reason="None")
def test_case_3(page):
    """
    1. Thực hiện di chuyển đến màn forgot password
    """
    login_page = LoginPage(page)
    login_page.go_to_login_page(base_url)
    login_page.go_to_forgot_password_page()

@pytest.mark.skip(reason="None")
def test_case_4(page):
    login_page = LoginPage(page)
    valid = creds["valid_user"]
    invalid = creds["locked_user"]
    login_page.go_to_login_page(base_url)
    login_page.login(valid["username"], valid["password"])
    login_page.verify_login_success()

def test_case_5(page):
    """
    1. login
    2. logout
    """   
    login_page = LoginPage(page)
    header_components = HeaderComponents(page)
    menu_bar_components = MenuBarComponents(page)
    valid = creds["valid_user"]
    login_page.go_to_login_page(base_url)
    login_page.login(valid["username"], valid["password"])
    login_page.verify_login_success()
    header_components._click_and_take_screenshot_all_button_in_header()
    menu_bar_components._click_and_take_screenshot_all_button_in_menu()
    header_components._logout()


