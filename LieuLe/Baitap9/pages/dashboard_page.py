import json
from core.base_page import BasePage
from playwright.sync_api import expect
from components.logout_component import LogoutComponent
from components.header.header_component import HeaderComponent
from components.left_menu.left_menu_component import LeftMenuComponent
from core.base_page import BasePage

from utils.config import LOGIN_URL

class DashboardPage(BasePage):
    LOGIN_URL = LOGIN_URL
    
    def __init__(self, page):
        super().__init__(page)
        self.component = LogoutComponent(page) 
        self.header = HeaderComponent(page)
        self.leftmenu = LeftMenuComponent(page)

    
    def logout (self):
        self._click(self.component.logout_btn)
        expect(self.page).to_have_url(self.LOGIN_URL)
    