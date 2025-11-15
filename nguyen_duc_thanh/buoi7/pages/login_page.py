from buoi7.pages.base_page import BasePage
from playwright.sync_api import expect
import time
class LoginPage(BasePage):
    URL = "https://hrm.anhtester.com/erp/login"
    WELCOME_LOGIN_TEXT = "//p[@class='text-muted']"
    USERNAME = "//input[@id='iusername']"
    PASSWORD = "//input[@id='ipassword']"
    LOGIN_BTN = "//button[@type='submit']"
    LOGIN_SUCCESS_TEXT = "//h2[@id='swal2-title']"
    LOGIN_FAILED_TEXT = "//div[@class='toast-message']"
    FORGOT_PASSWORD = "//span[normalize-space()='Forgot password?']"
    def __init__(self, page):
        super().__init__(page)

    def login(self,username,password):
        self.goto(self.URL)
        time.sleep(3)
        self.take_screenshot("access_url_successfully.png")
        self.send_text(self.USERNAME,username)
        self.send_text(self.PASSWORD,password)
        self.click_element(self.LOGIN_BTN)
    
    def assert_login_successful(self):
        expect(self.page).to_have_url("https://hrm.anhtester.com/erp/desk")

    def assert_login_failed(self):
        login_faild_text = self.get_locator(self.LOGIN_FAILED_TEXT)
        expect(login_faild_text).to_contain_text("Invalid Login Credentials.")

    def goto_forgot_password(self):
        self.goto(self.URL)
        self.click_element(self.FORGOT_PASSWORD)

    def assert_goto_forgot_password(self):
        expect(self.page).to_have_url("https://hrm.anhtester.com/erp/forgot-password")

    def assert_invalid_password(self):
        invalid_password = self.get_locator(self.LOGIN_FAILED_TEXT)
        expect(invalid_password).to_contain_text("Your password is too short, minimum 6 characters required.")
