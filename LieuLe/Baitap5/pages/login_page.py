from pages.base_page import BasePage
from playwright.async_api import expect

class LoginPage(BasePage):
    URL = "https://www.saucedemo.com/"
    Username = "#user-name"
    Password = "#password"
    Loginbtn = "#login-button"

    def __init__(self, page):
        super().__init__(page)

    def goto(self):
        self._visit(self.URL)

    def loginwith(self, username, password):
        self.goto()
        self._fill(self.Username, username)
        self._fill(self.Password, password)
        self._click(self.Loginbtn)

