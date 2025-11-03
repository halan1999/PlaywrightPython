from pages.login_page import LoginPage
from playwright.sync_api import Page

base_url = "https://hrm.anhtester.com/erp"
username = "admin_example"
password = "123456"

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

def test_case_3(page):
    """
    1. Thực hiện di chuyển đến màn forgot password
    """
    login_page = LoginPage(page)
    login_page.go_to_login_page(base_url)
    login_page.go_to_forgot_password_page()