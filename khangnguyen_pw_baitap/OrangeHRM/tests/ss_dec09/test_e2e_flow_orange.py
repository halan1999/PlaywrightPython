from playwright.sync_api import expect
from utils.read_json import read_json
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage


def test_orangehrm_e2e_flow(page):
    config = read_json("resources/credentials.json")
    login_url = config["orange_url"]
    username = config["username"]
    password = config["password"]

    # Open login page of Orange HRM
    login_page = LoginPage(page, login_url)
    login_page.open()

    # Verify X page of OrangeHRM
    x_page = login_page.open_x_page()
    x_page.is_x_page_orangehrm_loaded_with_X_logo_and_merchant_name_visible()
    x_page.take_screenshot("screenshots/x_page.png")

    # Back to login page in the first tab
    login_page.bring_to_front()

    # Login with valid username and password
    login_page.login(username, password)

    # Verify dashboard page is loaded (after login)
    dashboard_page = DashboardPage(page)
    dashboard_page.is_dashboard_page_loaded()
    dashboard_page.take_screenshot("screenshots/dashboard_page.png")
