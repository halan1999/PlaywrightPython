import json
from core.base_page import BasePage
from playwright.sync_api import expect

class LoginComponent(BasePage):
    USERNAME = "#iusername"
    PASSWORD = "#ipassword"
    LOGIN_BTN = "button[type='submit']"
    ERROR_MESSAGE = "//div[contains(@class,'toast-message')]"

    def __init__(self, page):
        super().__init__(page)