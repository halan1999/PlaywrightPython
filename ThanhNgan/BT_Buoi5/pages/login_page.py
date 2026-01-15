from pages.base_page import BasePage
from playwright.sync_api import Page, expect

class LoginPage(BasePage):
    URL = "https://www.saucedemo.com/"
    txt_username = "#user-name"
    txt_password = "#password"
    btn_login = "#login-button"

    # def __init__(self, page):
    #     super().__init__(page)

    # def goto(self):
    #     self._goto(self.URL)

    def login(self, username, password):
        self._goto(self.URL)
        self._fill(self.txt_username, username)
        self._fill(self.txt_password, password)
        self._click(self.btn_login)
        

