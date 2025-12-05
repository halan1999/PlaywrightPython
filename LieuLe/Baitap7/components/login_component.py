import json
from core.base_page import BasePage
from playwright.sync_api import expect

class LoginComponent(BasePage):
    username = "#iusername"
    password = "#ipassword"
    login_btn = "button[type='submit']"
    error_message = "//div[contains(@class,'toast-message')]"

    def __init__(self, page):
        super().__init__(page)