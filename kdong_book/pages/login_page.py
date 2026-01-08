from core.base_page import BasePage
from config.env_config import EnvConfig
print("LOGIN PAGE ENV FILE:", EnvConfig.__module__)

class LoginPage(BasePage):
    EMAIL_INPUT = '//input[@name="email"]'
    PASSWORD_INPUT = '//input[@name="password"]'
    LOGIN_BUTTON = '//button[normalize-space()="Login account"]'

    def __init__(self, page):
        self.page = page
        
    def open(self):
        self._visit("/sign-in")

    def login(self, email: str, password: str):
        self.page.fill(self.EMAIL_INPUT, email)
        self.page.fill(self.PASSWORD_INPUT, password)
        self.page.click(self.LOGIN_BUTTON)

    