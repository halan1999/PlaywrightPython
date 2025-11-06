from playwright.sync_api import Page, expect
from pages.base_page import BasePage
import re

class LoginPage(BasePage):
    URL = "https://hrm.anhtester.com/erp/login"

    def __init__(self, page: Page):
        super().__init__(page)
        self._username = page.locator("#iusername")
        self._password = page.locator("#ipassword")
        self._login_btn = page.locator('button[type="submit"]')
        self._toast_invalid = page.locator("#toast-container").get_by_text(re.compile("invalid", re.I))
        self._my_profile = page.locator('//a[contains(@href,"my-profile")]//p')

    def open(self):
        self.goto(self.URL)

    def is_loaded(self):
        expect(self._username).to_be_visible(timeout=5000)
        expect(self._password).to_be_visible(timeout=5000)
        return True

    def login(self, username: str, password: str):
        self.fill("#iusername", username)
        self.fill("#ipassword", password)
        self.click('button[type="submit"]')

    def is_invalid_toast_visible(self, timeout: int = 5000) -> bool:
        try:
            expect(self._toast_invalid).to_be_visible(timeout=timeout)
            return True
        except AssertionError:
            return False

    def is_logged_in(self, timeout: int = 8000) -> bool:
        try:
            expect(self._my_profile).to_be_visible(timeout=timeout)
            return True
        except AssertionError:
            return False
