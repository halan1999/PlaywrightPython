import json
from ..core.base_page import BasePage
from playwright.sync_api import expect

class LoginPage(BasePage):
    URL = "https://hrm.anhtester.com/erp/login"
    Username = "#iusername"
    Password = "#ipassword"
    Loginbtn = "button[type='submit']"
    Dasboard_url = "https://hrm.anhtester.com/erp/desk"
    Error_message = "//div[@class='toast-message']"


    def __init__(self, page, credential_path):
        super().__init__(page)    
        self.credential_path = credential_path

    def load_credentials(self, account_type = "valid"):
        with open(self.credential_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        creds = data.get(account_type)
        return creds["username"], creds["password"]
        
    def goto(self):
        self._visit(self.URL)

    def loginwith(self, account_type="valid"):
        username, password = self.load_credentials()
        self.goto()
        #self._take_screenshot("before_login.jpeg")
        self._fill(self.Username, username)
        self._fill(self.Password, password)
        self._click(self.Loginbtn)
        #self._take_screenshot("after_login.jpeg")

    def verify_login_success(self):
        expect(self.page).to_have_url(self.Dasboard_url)

    def get_error_message(self):
        locator = self.page.locator(self.Error_message)
        locator.first.wait_for(state="visible", timeout=3000)
        return locator.first.inner_text()