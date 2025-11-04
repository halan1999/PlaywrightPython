from .base_page import BasePage
from playwright.sync_api import expect
import time


class LoginPage(BasePage):
    URL = "https://www.saucedemo.com/"
    USERNAME_INPUT = 'input[data-test="username"]'
    PASSWORD_INPUT = 'input[data-test="password"]'
    LOGIN_BUTTON = 'input[data-test="login-button"]'
    ERROR_MESSAGE = 'h3[data-test="error"]'
    def visit_login_page(self):
        self._visit(self.URL)
    def login(self, username: str, password: str):
        self._fill(self.USERNAME_INPUT, username, "Username Input")
        self._fill(self.PASSWORD_INPUT, password, "Password Input")
        self._click(self.LOGIN_BUTTON, "Login Button")
        