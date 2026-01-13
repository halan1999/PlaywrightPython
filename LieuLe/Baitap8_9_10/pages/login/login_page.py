from playwright.sync_api import expect
from core.base_page import BasePage
from pages.dashboard.dashboard_page import DashboardPage
from components.login_component import LoginComponent
from components.login_footer_component import LoginFooterComponent
from config.urls import LOGIN_URL as LOGIN_PAGE_URL

class LoginPage(BasePage):

    LOGIN_URL = LOGIN_PAGE_URL
    def __init__(self, page):
        super().__init__(page)
        self.login_component = LoginComponent(page)
        self.footer_component = LoginFooterComponent(page)

    def open(self):
        self._visit(
            self.LOGIN_URL,
            wait_selector="input[name='username']"
        )
        #self.page.wait_for_load_state("networkidle")
        return self

    def login_valid_user(self):
        self.login_component.login_valid_user()
        return DashboardPage(self.page)
    
    def open_social_tabs(self):
        return self.footer_component.open_social_tabs()

    def verify_social_tabs(self, tabs):
        self.footer_component.verify_social_tabs(tabs)

    def open_twitter_tab(self):
        return self.footer_component.open_twitter_tab()

    def verify_twitter_page(self, twitter_page):
        self.footer_component.verify_twitter_page(twitter_page)

