from playwright.sync_api import expect
from pages.base_page import BasePage
import re

class XPage(BasePage):
    def __init__(self, page):
        super().__init__(page)

        self._x_logo = '//h1[@role="heading"]//a[@href="/"]'
        self.orangehrm_text = '//div[@data-testid="UserName"]//span[normalize-space()="OrangeHRM" and not(.//span) and not(@aria-hidden="true")]'

    def is_x_page_orangehrm_loaded(self):
        self.page.wait_for_load_state()
        expect(self.page.locator(self._x_logo)).to_be_visible()
        expect(self.page.locator(self.orangehrm_text)).to_be_visible()
