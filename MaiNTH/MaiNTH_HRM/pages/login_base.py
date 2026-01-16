from playwright.sync_api import expect 
from core.base_page import BasePage
import json,time
class LoginPage(BasePage):
    def __init__(self, page):
        super().__init__(page)

        self.URL = "https://hrm.anhtester.com/erp/login"
        self.username_input = "//input[@id='iusername']"
        self.password_input = "//input[@id='ipassword']"
        self.login_button = "//button[contains(@class, 'btn-primary')]"
        self.error_message = "//div[contains(@class,'toast-message')]"
        self.successful_popup = "//h2[contains(text(),'Logged In Successfully')]"

        
    def open_login_page(self):
        self.open(self.URL)

    def read_credentials(self, user_type):
        with open("data/credentials.json", "r", encoding="utf-8") as file:
            data = json.load(file)
            if user_type not in data:
                raise KeyError(f"⚠️ Không tìm thấy user_type '{user_type}' trong credentials.json")
            return data[user_type]
        
    
    def valid_user(self):
        creds = self.read_credentials("valid_user")
        self.fill(self.username_input, creds["username"])
        self.fill(self.password_input, creds["password"])
        self.click(self.login_button)
        # Verify successful login popup is displayed
        expect(self.page.locator(self.successful_popup)).to_be_visible()
        # Chờ cho đến khi trang load xong 
        self.page.wait_for_load_state("networkidle",timeout=10000)
        # chụp ảnh
        self._take_screenshot("after login successful")

    def invalid_user(self):
        creds = self.read_credentials("invalid_user")
        self.fill(self.username_input, creds["username"])
        self.fill(self.password_input, creds["password"])
        self.click(self.login_button)
        # Verify display error message
        self.assert_text(self.error_message,creds["errormessage"])
        # chụp ảnh
        self._take_screenshot("invalid_user")

    def blank_user(self):
        creds = self.read_credentials("blank_user")
        self.fill(self.username_input, creds["username"])
        self.fill(self.password_input, creds["password"])
        self.click(self.login_button)
        # Verify display error message
        self.assert_text(self.error_message,creds["errormessage"])
        # chụp ảnh
        self._take_screenshot("blank_user")

