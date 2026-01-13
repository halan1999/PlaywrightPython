from core.base_page import BasePage
from playwright.sync_api import expect


class DashboardPage(BasePage):
    LOGIN_SUCCESS_MESSAGE = '//p[contains(text(), "Login successfully.")]'
    def __init__(self, page):
        self.page = page

    def is_login_success_message_visible(self,timeout=5000) -> bool:
        try:
            expect(self.page.locator(self.LOGIN_SUCCESS_MESSAGE)).to_be_visible(timeout=timeout)
            return True
        except AssertionError:
            return False