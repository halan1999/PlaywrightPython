import json
from core.base_page import BasePage
from playwright.sync_api import expect

class LogoutComponent(BasePage):
    logout_btn = "//a[contains(text(), 'Logout')]"
    imag_avatar = "//img[@class = 'user-avtar']"
    logout_in_list = "//span[normalize-space() = 'Logout']"
    def __init__(self, page):
        super().__init__(page)