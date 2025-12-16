import json
from playwright.sync_api import expect

from core.base_page import BasePage
from components.logout_component import LogoutComponent
from components.header.header_component import HeaderComponent
from components.left_menu.left_menu_component import LeftMenuComponent
from utils.config import LOGIN_URL


class DashboardPage(BasePage):
    LOGIN_URL = LOGIN_URL

    def __init__(self, page):
        super().__init__(page)
        self.header = HeaderComponent(page)
        self.left_menu = LeftMenuComponent(page)
        self.logout = LogoutComponent(page)
       

    def do_logout(self):
        self._click(self.logout.logout_btn)
        expect(self.page).to_have_url(self.LOGIN_URL)
        print("Current page.url =", self.page.url)
