from playwright.sync_api import Page, expect
from pages.base_page import BasePage

class HomePage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self._profile_link = "//a[contains(@href,'my-profile')]//p"

        self._project_menu = '//a[normalize-space()="Home"]'
        self._log_out_button = '//div[@class="page-header"]//a[normalize-space()="Logout"]'

    def is_loaded(self):
        expect(self.page.locator(self._profile_link)).to_be_visible(timeout=5000)
        return True
    
    def is_project_menu_visible(self):
        expect(self.page.locator(self._project_menu)).to_be_visible(timeout=5000)
        return self

    def is_logout_button_visible(self):
        expect(self.page.locator(self._log_out_button)).to_be_visible(timeout=5000)
        return self
    
    def logout(self):
        self.page.locator(self._log_out_button).click()
