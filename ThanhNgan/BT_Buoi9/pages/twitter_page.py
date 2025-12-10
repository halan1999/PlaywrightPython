from core.base_page import BasePage
from playwright.sync_api import Page, expect
from pages.new_window_page import NewWindowPage
import json

class Orange_TwitterPage(BasePage):

    URL = "https://x.com/orangehrm?lang=en"
    HEADER_TITLE = "(//span[contains(text(),'Orange')])[1]"
    TEXT_UNDER_AVATAR = "(//span[contains(text(), 'OrangeHRM')])[2]"
    ICON = "//a[@href='/']"
    def __init__(self, page:Page):
        super().__init__(page)  

    def get_title_text(self) -> str:
        return self.page.title()