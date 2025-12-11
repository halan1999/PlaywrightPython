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

    def load_credential(self):
        with open(file= r"./BT_Buoi6/data/credentials.json", mode="r", encoding="utf-8") as file:
            credentials = json.load(file)
            return credentials["hrm_user"]
            
    def login(self, username, password):
        self._goto(self.URL)
        self._fill(self.txt_username, username)
        self._fill(self.txt_password, password)
        self._click(self.btn_login)
        dialog_success = "//h2[@id='swal2-title']"
        self.page.wait_for_selector(dialog_success)
        expect(self.page.locator(dialog_success)).to_be_visible()
        self._take_screenshot("after_login")

    def run_header_flow(self):
        self.header.click_all_items()   

    def logout(self):
        self.header.logout()

