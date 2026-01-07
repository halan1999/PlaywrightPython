from playwright.sync_api import Page, expect
from core.base_page import BasePage

class ProfilePage(BasePage):
    def __init__(self, page : Page, base_url : str):
        super().__init__(page)
        self.page = page
        self.base_url = base_url
        self.TXT_NAME = self.page.get_by_role("textbox", name = "Name", exact = True)

    def navigate_to_profile(self):
        self._navigate_url(self.base_url)
        

    def verify_name(self, name : str):
        expect(self.TXT_NAME).to_have_value(name)