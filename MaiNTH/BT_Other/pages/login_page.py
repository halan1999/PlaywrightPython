from core.base_page import BasePage
from playwright.sync_api import expect, Page
from components.header_component import Header_component
import time, json


class LoginPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.URL = "https://hrm.anhtester.com/erp/login"
        self.username_input = "//input[@id='iusername']"
        self.password_input = "//input[@id='ipassword']"
        self.login_button = "//button[contains(@class, 'btn-primary')]"
        self.error_message = "//div[contains(@class,'toast-message')]"
        self.successful_popup = "//h2[contains(text(),'Logged In Successfully')]"
        self.header = Header_component(page)


    # Load dữ liệu từ file Json
    def load_credentials(self, profile: str):
        with open("data/credentials.json", "r") as file:
            data = json.load(file)
            return data[profile]
        
    # Open page
    def open(self):
        self._open_url(self.URL)
        # self._take_screenshot("open_login_page_url",)

    # test user valid
    def login_valid_user(self):
        creds = self.load_credentials("valid_user")

        self._fill(self.username_input, creds["username"])
        self._fill(self.password_input, creds["password"])
        self._click(self.login_button)
       # Chờ toàn bộ trang load xong
        self.page.wait_for_load_state("networkidle", timeout=20000)

        # Chụp ảnh
        self._take_screenshot("after_login_successful")
        
        
    # test user invalid
    def login_with_invalidUser(self):
        creds = self.load_credentials("invalid_user")

        self._fill(self.username_input, creds["username"])
        self._fill(self.password_input, creds["password"])
        self._click(self.login_button)
        # Chờ toast hiển thị 
        self.page.wait_for_selector(self.error_message, timeout=5000)
        # Chụp ảnh
        self._take_screenshot("error_message_invalid_user")
        # Verify message hiển thị
        self._assert_text_visible(self.error_message, creds["errormessage"]
        )
        print("Display correct message in case wrong pw")

    # test user blank
    def login_with_blankUser(self):
        creds = self.load_credentials("blank_user")

        self._fill(self.username_input, creds["username"])
        self._fill(self.password_input, creds["password"])
        self._click(self.login_button)
        # Chờ toast hiển thị 
        self.page.wait_for_selector(self.error_message, timeout=5000)
        # Chụp ảnh
        self._take_screenshot("error_message_blank_user")
        # Verify
        self._assert_text_visible(self.error_message, creds["errormessage"]
        )
        print("Display correct message in case no input data")

    # Gọi hành động để click tất các các item trong header
    def run_header_flow(self):
        self.header.click_all_header_items()

    # Logout
    def logout(self):
        self.header.logout()
        self._take_screenshot("after_logout")








    def visit_login_page(self):
        self._visit(self.URL)
    def login(self, username: str, password: str):
        self._fill(self.USERNAME_INPUT, username, "Username Input")
        self._fill(self.PASSWORD_INPUT, password, "Password Input")
        self._click(self.LOGIN_BUTTON, "Login Button")