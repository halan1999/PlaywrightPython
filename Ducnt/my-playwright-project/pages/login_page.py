from cores.base_page import BasePage
from components.header_component import header_component
import json
from playwright.sync_api import expect

class LoginPage(BasePage):

    URL = "https://hrm.anhtester.com/erp/login"
    USERNAME_FIELD = "//input[@id='iusername']"
    PASSWORD_FIELD = "//input[@id='ipassword']"
    LOGIN_BUTTON = "//button[@type='submit']"
   

    def goto(self):
        self._visit(self.URL)
    
    def login(self, username: str, password: str):
        self.goto()

        self._fill(self.USERNAME_FIELD, username, "Username Field")
        self._fill(self.PASSWORD_FIELD, password, "Password Field")
        self._click(self.LOGIN_BUTTON, "Login Button")
        self.page.wait_for_load_state("networkidle")
       
    
    
    def assert_login_successful(self):
        
        expect(self.page).to_have_url("https://hrm.anhtester.com/erp/desk")
        self._take_screenshot("Loggin_successful.png")

    def logout(self):
       header = header_component(self.page)
       header._click(header.ACCOUNT, "Account Menu")
       header.page.wait_for_load_state("networkidle")
       header._click(header.Logout, "Logout Button")
       header.page.wait_for_load_state("networkidle")
    
    def assert_logout_successful(self):
        expect(self.page).to_have_url("https://hrm.anhtester.com/erp/login")
        self._take_screenshot("Logout_successful.png")


    # def assert_error_message_visible(self, expected_text):
    #     """Kiểm tra thông báo lỗi đăng nhập hiển thị đúng."""
    #     self._assert_text_visible(self.ERROR_MESSAGE, expected_text)