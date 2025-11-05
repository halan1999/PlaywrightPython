from BT_BUOI8.core.base_page import BasePage
from playwright.sync_api import expect

class LoginPage(BasePage):
    URL = "https://hrm.anhtester.com/"
    USERNAME_FIELD = "//input[@id='iusername']"
    PASSWORD_FIELD = "//input[@id='ipassword']"
    LOGIN_BUTTON = "//button[@type='submit']"

    def goto(self):
        self._visit(self.URL)

    def login(self, username, password):
        self.goto()
        self._take_screenshot("Open web.png")

        self._fill(self.USERNAME_FIELD, username)
        self._fill(self.PASSWORD_FIELD, password)
        self._click(self.LOGIN_BUTTON)

    def assert_login_successful(self):
        expect(self.page).to_have_url("https://hrm.anhtester.com/erp/desk")
        self._take_screenshot("Login_successful.png")

    # def assert_error_message_visible(self):
    #     self._assert_text_visible(self.ERROR_MESSAGE, "Sorry")