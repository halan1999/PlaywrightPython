from playwright.sync_api import expect
from utils.read_json import read_json
from pages.login_page import LoginPage
from pages.x_page import XPage
from pages.dashboard_page import DashboardPage


def test_orangehrm_e2e_flow(page):
    config = read_json("resources/credentials.json")
    login_url = config["orange_url"]
    username = config["username"]
    password = config["password"]

    # Open login page of Orange HRM
    login_page = LoginPage(page, login_url)
    login_page.open()

    # Declare another tab for X page
    with page.context.expect_page() as new_page_info:
        login_page.click_twitter_icon()
    x_tab = new_page_info.value

    # Verify X page of OrangeHRM
    x_page = XPage(x_tab)
    x_page.is_x_page_orangehrm_loaded()
    x_page.take_screenshot("screenshots/x_page.png")

    # Back to login page in the first tab
    login_page.bring_to_front()

    # Login with valid username and password
    login_page.login(username, password)

    # Verify dashboard page is loaded (after login)
    dashboard_page = DashboardPage(page)
    dashboard_page.is_dashboard_page_loaded()
    dashboard_page.take_screenshot("screenshots/dashboard_page.png")
