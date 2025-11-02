from playwright.sync_api import Page, expect
import re

class LoginPage:
    URL = "https://hrm.anhtester.com/erp/login"

    def __init__(self, page: Page):
        self.page = page

        self._username = page.locator("#iusername")
        self._password = page.locator("#ipassword")
        self._login_btn = page.locator('button[type="submit"]')

        self._toast_invalid = page.locator("#toast-container >> :text-matches('invalid', 'i')")

        self._my_profile = page.locator('//a[contains(@href,"my-profile")]//p')

    # Method: open URL
    def open(self):
        self.page.goto(self.URL)

    # Method: login
    def login(self, username: str, password: str):
        self._username.fill(username)
        self._password.fill(password)
        self._login_btn.click()

    # Method: check invalid toast message visible 
    def is_invalid_toast_visible(self, timeout: int = 5000) -> bool:
        try:
            expect(self._toast_invalid).to_be_visible(timeout=timeout)
            return True
        except AssertionError:
            return False

    # Method: check logged in state
    def is_logged_in(self, timeout: int = 8000) -> bool:
        try:
            expect(self._my_profile).to_be_visible(timeout=timeout)
            return True
        except AssertionError:
            return False