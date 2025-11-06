from ..pages.base_page import BasePage
from playwright.sync_api import sync_playwright, Playwright, expect

class LoginPage(BasePage):
    URL = "https://www.saucedemo.com/"
    Username = "#user-name"
    Password = "#password"
    Loginbtn = "#login-button"
    Errorrmess = "//h3[@data-test = 'error']"

    def __init__(self, page):
        super().__init__(page)  
        self.page = page
        
    def goto(self):
        self._visit(self.URL)

    def loginwith(self, username, password):
        self.goto()
        self._fill(self.Username, username)
        self._fill(self.Password, password)
        self._click(self.Loginbtn)

    def get_error_message(self):
        return self.page.locator(self.Errorrmess)
