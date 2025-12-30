from playwright.sync_api import expect
from pages.base_page import BasePage
import re

class XPage(BasePage):
    # Locators
    _x_logo = '//h1[@role="heading"]//a[@href="/"]'
    _orangehrm_text = '//div[@data-testid="UserName"]//span[normalize-space()="OrangeHRM" and not(.//span) and not(@aria-hidden="true")]'
    
    def __init__(self, page):
        super().__init__(page)

    def is_x_page_orangehrm_loaded_with_X_logo_and_merchant_name_visible(self):
        self.page.wait_for_load_state()
        expect(self.page.locator(self._x_logo)).to_be_visible()
        expect(self.page.locator(self._orangehrm_text)).to_be_visible()
