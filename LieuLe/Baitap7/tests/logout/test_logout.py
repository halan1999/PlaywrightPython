from playwright.sync_api import Playwright
from pages.dashboard_page import DashboardPage
from pages.login_page import LoginPage

def test_logout(logged_in_page, dashboard_page):
    dashboard_page.page = logged_in_page
    dashboard_page.logout()
