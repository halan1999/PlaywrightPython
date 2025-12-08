from playwright.sync_api import Page
from Core.Base_page import BasePage
class HeaderPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
    def logout(self):
        self.page.get_by_role("button", name="admin_example hello").click()
        self.page.get_by_role("link", name="Logout", exact=True).click()
    
        