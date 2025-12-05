import json
from core.base_page import BasePage
from playwright.sync_api import expect
from components.login_component import LoginComponent
from utils.config import LOGIN_URL, DESK_URL

CREDENTIAL_PATH = "Baitap7/data/login_acc.json"
class LoginPage(BasePage):
    LOGIN_URL = LOGIN_URL
    DASHBOARD_URL = DESK_URL
    def __init__(self, page):
        super().__init__(page)
        self.credential_path = CREDENTIAL_PATH 
        self.component = LoginComponent(page) 

    def load_credentials(self, account_type = "valid"):
        with open(self.credential_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        creds = data.get(account_type)
        return creds["username"], creds["password"]
        
    def open(self):
        self._visit(self.LOGIN_URL)
        
    def login_valid_user(self, account_type = "valid"):
        username, password = self.load_credentials(account_type)
        self.open()
        self._fill(self.component.username, username)
        self._fill(self.component.password, password) 
        self._click(self.component.login_btn)
        
    def login_invalid_user(self, account_type = "invalid"):
        username, password = self.load_credentials(account_type)
        self.open()
        self._fill(self.component.username, username)
        self._fill(self.component.password, password)
        self._click(self.component.login_btn)
        
    def verify_login_success(self):
        expect(self.page).to_have_url(self.DASHBOARD_URL)

    def get_error_message(self):
        locator = self.page.locator(self.component.error_message)
        locator.first.wait_for(state="visible", timeout=3000)
        return locator.first.inner_text()