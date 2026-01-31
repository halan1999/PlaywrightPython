from BT_BUOI7.pages.base_page import BasePage
from playwright.sync_api import expect

class LoginPage(BasePage):
    URL = "https://www.saucedemo.com/"
    USERNAME_FIELD = "//input[@placeholder='Username']"
    PASSWORD_FIELD = "//input[@placeholder='Password']"
    LOGIN_BUTTON = "//input[@type='submit']"
    ERROR_MESSAGE = "//h3[@data-test='error']"

    def goto(self):
        self._visit(self.URL)

    def login(self, username, password):
        self.goto()
        self._fill(self.USERNAME_FIELD, username)
        self._fill(self.PASSWORD_FIELD, password)
        self._click(self.LOGIN_BUTTON)

    def assert_login_successful(self):
        expect(self.page).to_have_url("https://www.saucedemo.com/inventory.html")

    def assert_error_message_visible(self):
        self._assert_text_visible(self.ERROR_MESSAGE, "Sorry")