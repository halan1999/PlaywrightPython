from core.base_page import BasePage
from components.header_component import HeaderComponent
from playwright.sync_api import Page, expect
import time, json
class LoginPage(BasePage):

    URL = "https://hrm.anhtester.com/erp/login"
    txt_username = "#iusername"
    txt_password = "#ipassword"
    btn_login = "//button[@type='submit']"
    
    def __init__(self, page):
        super().__init__(page)
        self.header = HeaderComponent(page)

    def goto(self):
        self._goto(self.URL)
        self._take_screenshot("login_page")

    def load_credential(self, type:str):
        with open(file= r"./BT_Buoi7/data/credentials.json", mode="r", encoding="utf-8") as file:
            credentials = json.load(file)
            return credentials[type]
            
    def login_with_valid_user(self):
        valid_credential = self.load_credential("hrm_user")
        self._fill(self.txt_username, valid_credential["username"])
        self._fill(self.txt_password, valid_credential["password"])
        self._click(self.btn_login)
        dialog_success = "//h2[@id='swal2-title']"
        self.page.wait_for_selector(dialog_success)
        expect(self.page.locator(dialog_success)).to_be_visible()
        expect(self.page.locator(dialog_success)).to_contain_text("Logged In Successfully.")
        self._take_screenshot("login_successfully")

    def login_with_invalid_user(self):
        invalid_credential = self.load_credential("hrm_invalid_user")
        self._fill(self.txt_username, invalid_credential["username"])
        self._fill(self.txt_password, invalid_credential["password"])
        self._click(self.btn_login)
        toast_error = "//div[@class='toast toast-error']"
        toast_message = "//div[@class='toast-message']"
        expect(self.page.locator(toast_error)).to_be_visible()
        expect(self.page.locator(toast_message)).to_contain_text("Invalid Login Credentials.")
        self._take_screenshot("login_failed")

    def login_with_empty_credential(self):
        credential = self.load_credential("hrm_empty_credential")
        self._fill(self.txt_username, credential["username"])
        self._fill(self.txt_password, credential["password"])
        self._click(self.btn_login)
        toast_error = "//div[@class='toast toast-error']"
        toast_message = "//div[@class='toast-message']"
        expect(self.page.locator(toast_error)).to_be_visible()
        expect(self.page.locator(toast_message)).to_contain_text("The username field is required.")
        self._take_screenshot("login_failed_empty_credential")


    def run_header_flow(self):
        self.header.click_all_items()   

    def logout(self):
        self.header.logout()

