from .base_page import BasePage
from playwright.sync_api import expect
import time

class LoginPage(BasePage):

    URL = "https://www.saucedemo.com/"
    USERNAME_FIELD = "#user-name"
    PASSWORD_FIELD = "#password"
    LOGIN_BUTTON = "#login-button"
    ERROR_MESSAGE = "[data-test='error']"

    def goto(self):
        self._visit(self.URL)

    def login(self, username, password):
        self.goto()
        self._fill(self.USERNAME_FIELD, username, name="Username")
        self._fill(self.PASSWORD_FIELD, password, name="Password")
        self._click(self.LOGIN_BUTTON, name="Login Button")

    def assert_login_successful(self):
        expect(self.page).to_have_url("https://www.saucedemo.com/inventory.html")

    def assert_error_message_visible(self, expected_text):
        self._assert_text_visible(self.ERROR_MESSAGE, expected_text)