from playwright.sync_api import Page
from core.common_locators import CommonLocators
from core.base_page import BasePage
from components.header_components import HeaderComponents
from utils.messages import ERROR_MESSAGE

class LoginPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.page = page
        self.header = HeaderComponents(page)
        self.username_input_locator = CommonLocators._input_by_attribute_xpath("id", "iusername")
        self.password_input_locator = CommonLocators._input_by_attribute_xpath("id", "ipassword")
        self.login_button_locator = CommonLocators._button_by_attribute_xpath("type", "submit")
        self.forgot_password_link_locator = CommonLocators._contains_text_xpath("span", "Forgot password?")
        #---------Message-----------
        self.toast_message_invalid_credentials = CommonLocators._contains_text_xpath("div", f"{ERROR_MESSAGE['LOGIN']['INVALID_CREDENTIALS']}")
        self.toast_message_error_password_too_short = CommonLocators._contains_text_xpath("div", f"{ERROR_MESSAGE['LOGIN']['ERROR_PASSWORD_TOO_SHORT']}")
        self.toast_message_required = CommonLocators._contains_text_xpath("div", f"{ERROR_MESSAGE['LOGIN']['REQUIRED_USERNAME_PASSWORD']}")

    def go_to_login_page(self, base_url):
        self._goto(f"{base_url}/login")
        self._take_screenshot("go_to_login_page")

    def login(self, username: str, password: str):
        self._fill(self.username_input_locator, username)
        self._fill(self.password_input_locator, password)
        self._click(self.login_button_locator)

    def verify_login_success(self):
        self._expect_to_have_url("/desk")
        self._take_screenshot("should_be_login")

    def verify_login_failure_invalid_credentials(self):
        self._expect_to_be_visible(self.toast_message_invalid_credentials)
        self._take_screenshot("Non_login")

    def verify_login_failure_password_too_short(self):
        self._expect_to_be_visible(self.toast_message_error_password_too_short)
        self._take_screenshot("password_too_short")

    def verify_login_failure_required(self):
        self._expect_to_be_visible(self.toast_message_required)
        self._take_screenshot("required")

    def go_to_forgot_password_page(self):
        self._click(self.forgot_password_link_locator)
        self._expect_to_have_url("/forgot-password")

    def run_header_flow(self):
        self.header._click_and_take_screenshot_all_button_in_header()
