from core.base_page import BasePage
from playwright.sync_api import expect
import time, re, json

class LoginPage(BasePage):
    URL = "https://hrm.anhtester.com/erp/login"
    USERNAME = "#iusername"
    PASSWORD = "#ipassword"
    TEXT_BTN_FORGOT_PASSWORD = "//div//a[@href='https://hrm.anhtester.com/erp/forgot-password']"
    BTN_LOGIN = "//div//button[@type='submit']"
    ERROR_MESSAGE = "[data-test='error']"

    def goto(self):
        self._navigate_to_page(self.URL)
        self._take_screenshots("login_page.png")

    def load_data_login(self):
        with open("resources/data_login.json", "r") as file:
            return json.load(file)

    def login_withUsernamePassword(self):
        data_login = self.load_data_login()
        self.goto()
        self._fill_data(self.USERNAME, data_login['username'])
        self._fill_data(self.PASSWORD, data_login['password'])
        self._click_on_object(self.BTN_LOGIN)
        time.sleep(3)
        self._take_screenshots("logged_in_page.png")
    
    def assert_login_successfully(self):
        expect(self.page).to_have_url("https://hrm.anhtester.com/erp/desk")

    def assert_login_failed(self):
        self._assert_text_visible(self.ERROR_MESSAGE)

    
    
