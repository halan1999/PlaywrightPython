from playwright.sync_api import expect

from buoi5.pages.base_page import BasePage

class LoginPage(BasePage):

    URL = "https://www.saucedemo.com/"
    USERNAME = "//input[@id='user-name']"
    PASSWORD = "//input[@id='password']"
    LOGIN_BUTTON = "//input[@id='login-button']"
    ERROR_MESSAGE = "[data-test='error']"

    def goto(self):
        self._visit(self.URL)
    
    def login(self,username,password):
        self.goto()
        self._fill(self.USERNAME, username, name="Username")
        self._fill(self.PASSWORD, password, name="Password")
        self._click(self.LOGIN_BUTTON, name="Login Button")
    
    def assert_login_successful(self):
        expect(self.page).to_have_url("https://www.saucedemo.com/inventory.html")

    def assert_error_message_visible(self, expected_text):
        self._assert_text_visible(self.ERROR_MESSAGE, expected_text)