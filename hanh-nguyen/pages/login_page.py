from core.base_page import BasePage
from playwright.sync_api import expect
import time

class LoginPage(BasePage):
    URL = "https://hrm.anhtester.com/erp/login/"
    username_field = "#iusername"
    password_field = "#ipassword"
    login_button = "//button[@type = 'submit']"

    def __init__(self, page):
        super().__init__(page)
        self.header = HeaderComponent(Page)

    def load_credentials(self):
        with open("D:\PlaywrightPython\hanh-nguyen\data\credentials.json")
        return 

    def open(self):
        self._open_url(self.URL)
        self._take_screenshot("login_page.png")

    def login(self, username, password):
        creds = self.load_credentials()
        self._fill(self.username_field, username, name = "admin_example")
        self._fill(self.password_field, password, name = "123456")
        self._click(self.login_button, name = "Login")

    def assert_login_successful(self):
        expect(self.page).to_have_url("https://hrm.anhtester.com/erp/desk")
        self._take_screenshot("home_page.png")


    def assert_error_message_visible(self, expected_text):
        self._assert_text_visible(self.error_message, expected_text)

    time.sleep(5)