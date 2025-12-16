from playwright.sync_api import expect
from pages.base_page import BasePage


class DashboardPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.dashboard_text = '//h6[text()="Dashboard"]'

    def is_dashboard_page_loaded(self):
        expect(self.page.locator(self.dashboard_text)).to_be_visible()