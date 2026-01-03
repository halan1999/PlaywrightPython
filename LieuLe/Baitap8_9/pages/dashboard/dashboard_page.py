import re
from playwright.sync_api import expect
from components.user_menu_component import UserMenuComponent

DASHBOARD_TITLE = "//h6[normalize-space()='Dashboard']"

class DashboardPage:
    def __init__(self, page):
        self.page = page
        self.user_menu = UserMenuComponent(page)

    def verify_dashboard_displayed(self):
        expect(self.page).to_have_url(re.compile("dashboard"))
        expect(self.page.locator(DASHBOARD_TITLE)).to_be_visible()
       