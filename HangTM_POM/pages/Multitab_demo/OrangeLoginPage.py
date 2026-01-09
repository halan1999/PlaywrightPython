from playwright.sync_api import Page
from Core.config import ORG_URL, ORG_USERNAME, ORG_PASSWORD
from Core.Base_page import BasePage
class OrangeLoginPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.page=page
    # Mở trang login:
    def open(self):
        self.page.goto(ORG_URL)
    # icon footer
    def linkedin_icon(self):
        return self.page.locator("div.orangehrm-login-footer-sm a[href*='linkedin']")
    def facebook_icon(self):
        return self.page.locator("div.orangehrm-login-footer-sm a[href*='facebook']")
    def twitter_icon(self):
        return self.page.locator("div.orangehrm-login-footer-sm a[href*='twitter']")
    def youtube_icon(self):
        return self.page.locator("div.orangehrm-login-footer-sm a[href*='youtube']")
    #login
    def username_input(self):
        return self.page.locator("input[name=username]")
    def password_input(self):
        return self.page.locator("input[name=password]")
    def Login_button(self):
        return self.page.locator("button[type='submit']")
    def login(self, username:str=ORG_USERNAME, password:str=ORG_PASSWORD):
        self.username_input().fill(username)
        self.password_input().fill(password)
        self.Login_button().click()
   

        