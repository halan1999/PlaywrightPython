import re
from playwright.sync_api import expect
from components.user_menu_component import UserMenuComponent

class DashboardPage:
    DASHBOARD_TITLE = "//h6[normalize-space()='Dashboard']"
    def __init__(self, page):
        self.page = page
        self.user_menu = UserMenuComponent(page)

    def verify_dashboard_displayed(self):
        expect(self.page).to_have_url(re.compile("dashboard"), timeout=10000)
        expect(self.page.locator(self.DASHBOARD_TITLE)).to_be_visible()
       