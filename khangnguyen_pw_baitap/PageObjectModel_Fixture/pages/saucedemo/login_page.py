from playwright.sync_api import Page, expect
from pages.base_page import BasePage


class LoginPage(BasePage):
    # Locators
    _username_input = '//input[@id="user-name"]'
    _password_input = '//input[@id="password"]'
    _login_button = '//input[@id="login-button"]'
    _locked_out_error = '//h3[normalize-space()="Epic sadface: Sorry, this user has been locked out."]'

    URL = "https://www.saucedemo.com/"

    def __init__(self, page: Page):
        super().__init__(page)

    def open(self):
        self.page.goto(self.URL)

    def login(self, username: str, password: str):
        self.page.fill(self._username_input, username)
        self.page.fill(self._password_input, password)
        self.page.click(self._login_button)

    def is_login_failed(self) -> bool:
        return self.page.locator(self._locked_out_error).is_visible()
