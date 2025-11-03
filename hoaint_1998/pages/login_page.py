from playwright.sync_api import Page
from locators.login_page_locators import LoginPageLocators
from pages.base_page import BasePage

class LoginPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.page = page
        self.username_input_locator = LoginPageLocators.USERNAME_INPUT_LOCATOR
        self.password_input_locator = LoginPageLocators.PASSWORD_INPUT_LOCATOR
        self.login_button_locator = LoginPageLocators.LOGIN_BUTTON_LOCATOR
        self.forgot_password_link_locator = LoginPageLocators.FORGOT_PASSWORD_LINK_LOCATOR
        #---------Message-----------
        self.toast_error_invalid_credentials = LoginPageLocators.TOAST_ERROR_INVALID_CREDENTIALS

    def go_to_login_page(self, base_url):
        self._goto(f"{base_url}/login")

    def login(self, username: str, password: str):
        self._fill(self.username_input_locator, username)
        self._fill(self.password_input_locator, password)
        self._click(self.login_button_locator)

    def verify_login_success(self):
        self._expect_to_have_url("/desk")

    def verify_login_failure_invalid_credentials(self):
        self._expect_to_be_visible(self.toast_error_invalid_credentials)

    def go_to_forgot_password_page(self):
        self._click(self.forgot_password_link_locator)
        self._expect_to_have_url("/forgot-password")
