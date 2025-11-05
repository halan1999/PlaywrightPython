import json
from core.base_page import BasePage
from playwright.async_api import expect

class LoginPage(BasePage):
    URL = "https://hrm.anhtester.com/erp/login"
    Username = "#iusername"
    Password = "#ipassword"
    Loginbtn = "//i[contains(@class, 'fas fa-user-lock d-blockd')]"

    def __init__(self, page):
        super().__init__(page)

    def load_credentials(self, filepath="data/credentials.json"):
        with open(filepath, "r", encoding="utf-8") as f:
            data = json.load(f)
        return data["username"], data["password"]

    def goto(self):
        self._visit(self.URL)

    def loginwith(self, username, password):
        self.goto()
        self._fill(self.Username, username)
        self._fill(self.Password, password)
        self._click(self.Loginbtn)
    
