from playwright.sync_api import expect 
from utils.config import LOGIN_URL
from core.base_page import BasePage
from components.header.header_menu_component import HeaderMenuComponent
from components.left_menu.left_menu_component import LeftMenuComponent
from components.logout_component import LogoutComponent

class DashboardPage(BasePage):

    def __init__(self, page):
        super().__init__(page)
        self.header_menu = HeaderMenuComponent(page)  
        self.left_menu = LeftMenuComponent(page) 
        self.logout_component = LogoutComponent(page)

    def do_logout(self, via="header"):
        if via == "header":
            self.logout_component.logout_from_header()
        elif via == "body":
            self.logout_component.logout_from_body()
        else:
            raise ValueError(f"Unknown logout method: {via}")

        expect(self.page).to_have_url(LOGIN_URL)
