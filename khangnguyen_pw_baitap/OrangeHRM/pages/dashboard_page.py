from playwright.sync_api import expect
from pages.base_page import BasePage


class DashboardPage(BasePage):
    # Locators
    _dashboard_text = '//h6[text()="Dashboard"]'
    
    def __init__(self, page):
        super().__init__(page)
        
    def is_dashboard_page_loaded(self):
        expect(self.page.locator(self._dashboard_text)).to_be_visible()
