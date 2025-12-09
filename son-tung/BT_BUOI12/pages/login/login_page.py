import json

from BT_BUOI8.components.header.header_component import HeaderComponent
from BT_BUOI8.core.base_page import BasePage
from playwright.sync_api import expect

class LoginPage(BasePage):
    URL = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    USERNAME_FIELD = "//input[@id='iusername']"
    PASSWORD_FIELD = "//input[@id='ipassword']"
    LOGIN_BUTTON = "//button[@type='submit']"
    ERROR_MESSAGE = "//div[@class='toast-message']"

    def __init__(self, page):
        super().__init__(page)
        self.header = HeaderComponent(page)

    def goto(self):
        self._visit(self.URL)
        self._take_screenshot("Open_web.png")

    def login_user(self, account):
        self.goto()

        with open("BT_BUOI8/data/users.json") as f:
            user = json.load(f)

        login = user[account]

        self._fill(self.USERNAME_FIELD, login["username"])
        self._fill(self.PASSWORD_FIELD, login["password"])
        self._click(self.LOGIN_BUTTON)

        self._take_screenshot("Login_user.png")

    def assert_login_successful(self):
        expect(self.page).to_have_url("https://hrm.anhtester.com/erp/desk")
        self._take_screenshot("Login_successful.png")

    def assert_error_message_visible(self):
        expect(self._get_locator(self.ERROR_MESSAGE)).to_be_visible()
        self._take_screenshot("Login_failed.png")

    def open_all_button_via_header(self):
        self.header.open_all_button()

    def open_app_list_via_header(self):
        self.header.open_app_list_button()

    def open_language_list_via_header(self):
        self.header.open_language_list_button()

    def logout(self):
        self.header.logout()
