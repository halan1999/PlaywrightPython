from core.base_page import BasePage
from playwright.sync_api import Page, expect

class NewWindowPage(BasePage):

    def __init__(self, page:Page):
        super().__init__(page)
    
    # def get_heading_text(self) -> str:
    #     return self._get_text(self.HEADING)
    
    def get_title_page(self) -> str:
        return self.page.title()    