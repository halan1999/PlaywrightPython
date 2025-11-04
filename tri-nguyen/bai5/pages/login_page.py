from pages.base_page import BasePage
from playwright.sync_api import expect
import time, re

class LoginPage(BasePage):
    URL = "https://hrm.anhtester.com/erp/login"
    USERNAME = "#iusername"
    PASSWORD = "#ipassword"
    TEXT_BTN_FORGOT_PASSWORD = "//div//a[@href='https://hrm.anhtester.com/erp/forgot-password']"
    BTN_LOGIN = "//div//button[@type='submit']"
    ERROR_MESSAGE = "[data-test='error']"

    def goto(self):
        self._navigate_to_page(self.URL)

    def login_withUsernamePassword(self, username, password):
        self.goto()
        self._fill_data(self.USERNAME, username)
        self._fill_data(self.PASSWORD, password)
        self._click_on_object(self.BTN_LOGIN)
    
    def assert_login_successfully(self):
        expect(self.page).to_have_url("https://hrm.anhtester.com/erp/desk")

    def assert_login_failed(self):
        self._assert_text_visible(self.ERROR_MESSAGE)
    time.sleep(5)
    
