from playwright.async_api import Page
from Core.config import ORG_URL
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
   

        