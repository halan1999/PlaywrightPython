from core.base_page import BasePage
from playwright.sync_api import expect
import time


class LoginHrmPage(BasePage):
    URL = "https://hrm.anhtester.com/erp/login"
    USERNAME_INPUT = "//input[@id='iusername']"
    PASSWORD_INPUT = "//input[@id='ipassword']"
    LOGIN_BUTTON = "//span[@class='ladda-label']"
    ERROR_MESSAGE = "h3[data-test='error']"
    def visit_login_page(self):
        self._visit(self.URL)
    def login(self, username: str, password: str):
        self._fill(self.USERNAME_INPUT, username, "Username Input")
        self._fill(self.PASSWORD_INPUT, password, "Password Input")
        self._click(self.LOGIN_BUTTON, "Login Button")