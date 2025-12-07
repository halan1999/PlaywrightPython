from playwright.sync_api import Page
from core.common_locators import CommonLocators
from core.base_page import BasePage
from components.header_components import HeaderComponents
from utils.messages import ERROR_MESSAGE
from locators.login.login_locators import LoginLocators as LL

class LoginPage(BasePage):
        
    def __init__(self, page):
        super().__init__(page)
        self.page = page
        self.header = HeaderComponents(page)
        

    def go_to_login_page(self, base_url):
        self._goto(f"{base_url}/login")
        self._take_screenshot("go_to_login_page")

    def login(self, username: str, password: str):
        self._fill(LL.USERNAME_INPUT, username)
        self._fill(LL.PASSWORD_INPUT, password)
        self._click(LL.LOGIN_BUTTON)

    def verify_login_success(self):
        self._expect_to_have_url("/desk")
        self.page.wait_for_load_state("load")
        self._take_screenshot("should_be_login")

    def verify_login_failure_invalid_credentials(self):
        self._expect_to_be_visible(LL.TOAST_MESSAGE_INVALID_CREDENTIALS)
        self._take_screenshot("Non_login")

    def verify_login_failure_password_too_short(self):
        self._expect_to_be_visible(LL.TOAST_MESSAGE_ERROR_PASSWORD_TOO_SHORT)
        self._take_screenshot("password_too_short")

    def verify_login_failure_required(self):
        self._expect_to_be_visible(LL.TOAST_MESSAGE_REQUIRED)
        self._take_screenshot("required")

    def go_to_forgot_password_page(self):
        self._click(LL.FORGOT_PASSWORD_LINK)
        self._expect_to_have_url("/forgot-password")

    def run_header_flow(self):
        self.header._click_and_take_screenshot_all_button_in_header()
