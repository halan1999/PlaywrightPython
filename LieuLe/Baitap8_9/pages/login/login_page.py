from LieuLe.Baitap8_9.components.login_component import LoginComponent
from LieuLe.Baitap8_9.components.login_footer_component import LoginFooterComponent
from LieuLe.Baitap8_9.config.urls import LOGIN_URL
from LieuLe.Baitap8_9.pages.dashboard.dashboard_page import DashboardPage

class LoginPage:
    def __init__(self, page):
        self.page = page
        self.login_component = LoginComponent(page)
        self.footer_component = LoginFooterComponent(page)
        self.dashboard_page = DashboardPage(page)
        
    def open(self):
        self.page.goto(LOGIN_URL)

    def login_valid_user(self):
        self.login_component.login_valid_user()
        return self.dashboard_page

    def open_social_tabs(self):
        return self.footer_component.open_social_tabs()

    def verify_social_tabs(self, tabs):
        self.footer_component.verify_social_tabs(tabs)

    def open_twitter_tab(self):
        return self.footer_component.open_twitter_tab()

    def verify_twitter_page(self, twitter_page):
        return self.footer_component.verify_twitter_page(twitter_page)
    