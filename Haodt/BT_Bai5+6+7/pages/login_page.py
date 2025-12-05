import json
from core.base_page import BasePage
from components.header_component import HeaderComponent
from playwright.sync_api import Page,expect

class LoginPage(BasePage):
    URL="https://hrm.anhtester.com/erp/login"

    username_input="//input[@id='iusername']"
    password_input="//input[@id='ipassword']"
    login_button="//button[contains(@class,'btn-primary')]"

    def __init__(self, page:Page):
        super().__init__(page)
        self.header=HeaderComponent(page)

    def load_credentials(self):
        with open("data/credentials.json","r") as file:
            return json.load(file)
        
    def open(self):
        self._open_url(self.URL)
        self._take_screenshot("open_login_page")

    def login_valid_user(self):
        creds=self.load_credentials()

        self._fill(self.username_input,creds["username"])
        self._fill(self.password_input,creds["password"])
        self._click(self.login_button)

        self._take_screenshot("affter_login")

    def login_with_invalidUser(self):
        creds=self.load_credentials()

        self._fill(self.username_input,creds["username"])
        self._fill(self.password_input,creds["password"])
        self._click(self.login_button)

        self._take_screenshot("error_message")
        #self._assert_text_visible()

    def run_header_flow(self):
        self.header.click_all_header_items()
    
    def run_menu(self):
        self.header.click_all_menu_items()

    def logout(self):
        self.header.logout()
        self._take_screenshot("after_logout")
        