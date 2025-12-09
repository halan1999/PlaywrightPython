from playwright.sync_api import Page
class LoginPage:

    def __init__(self, page: Page):
        self.page = page
        self.social_icons = page.locator("div.orangehrm-login-footer-sm a")

    def goto(self):
        self.page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    def get_social_icon_by_index(self, index: int):
        return self.social_icons.nth(index - 1)

    def get_all_social_icons(self):
        """Trả về toàn bộ locator social icon"""
        return self.social_icons
    


