from playwright.sync_api import Page
from core.base_page import BasePage

class LoginPage(BasePage):

    URL = "https://hrm.anhtester.com"
    INPUT_USERNAME = "#iusername"
    INPUT_PASSWORD = "#ipassword"
    LOGIN_BUTTON = "//button[contains(@class,'primary')]"

    def __init__(self, page):
        super().__init__(page)

    def open_url(self):
        self.open(self.URL)

    def login(self, username: str, password: str):
        self.fill.username(self.INPUT_USERNAME, username)
        self.fill.password(self.INPUT_PASSWORD, password)
        self.click(self.LOGIN_BUTTON)
        
