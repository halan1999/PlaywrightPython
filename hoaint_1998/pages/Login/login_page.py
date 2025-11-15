from playwright.sync_api import Page
from core.common_locators import CommonLocators
from core.base_page import BasePage
from components.header_components import HeaderComponents
from utils.messages import ERROR_MESSAGE

class LoginPage(BasePage):
    USERNAME_INPUT = CommonLocators._input_by_attribute_xpath("id", "iusername")
    PASSWORD_INPUT = CommonLocators._input_by_attribute_xpath("id", "ipassword")
    LOGIN_BUTTON = CommonLocators._button_by_attribute_xpath("type", "submit")
    FORGOT_PASSWORD_LINK = CommonLocators._contains_text_xpath("span", "Forgot password?")
    #---------Message-----------
    TOAST_MESSAGE_INVALID_CREDENTIALS = CommonLocators._contains_text_xpath("div", f"{ERROR_MESSAGE['LOGIN']['INVALID_CREDENTIALS']}")
    TOAST_MESSAGE_ERROR_PASSWORD_TOO_SHORT = CommonLocators._contains_text_xpath("div", f"{ERROR_MESSAGE['LOGIN']['ERROR_PASSWORD_TOO_SHORT']}")
    TOAST_MESSAGE_REQUIRED = CommonLocators._contains_text_xpath("div", f"{ERROR_MESSAGE['LOGIN']['REQUIRED_USERNAME_PASSWORD']}")
    #      
    def __init__(self, page):
        super().__init__(page)
        self.page = page
        self.header = HeaderComponents(page)
        

    def go_to_login_page(self, base_url):
        self._goto(f"{base_url}/login")
        self._take_screenshot("go_to_login_page")

    def login(self, username: str, password: str):
        self._fill(self.USERNAME_INPUT, username)
        self._fill(self.PASSWORD_INPUT, password)
        self._click(self.LOGIN_BUTTON)

    def verify_login_success(self):
        self._expect_to_have_url("/desk")
        self._take_screenshot("should_be_login")

    def verify_login_failure_invalid_credentials(self):
        self._expect_to_be_visible(self.TOAST_MESSAGE_INVALID_CREDENTIALS)
        self._take_screenshot("Non_login")

    def verify_login_failure_password_too_short(self):
        self._expect_to_be_visible(self.TOAST_MESSAGE_ERROR_PASSWORD_TOO_SHORT)
        self._take_screenshot("password_too_short")

    def verify_login_failure_required(self):
        self._expect_to_be_visible(self.TOAST_MESSAGE_REQUIRED)
        self._take_screenshot("required")

    def go_to_forgot_password_page(self):
        self._click(self.FORGOT_PASSWORD_LINK)
        self._expect_to_have_url("/forgot-password")

    def run_header_flow(self):
        self.header._click_and_take_screenshot_all_button_in_header()
