from playwright.sync_api import Page, expect
from core.base_page import BasePage

class XPage(BasePage):
    def __init__(self, page):
        super().__init__(page)

    def verify_x_icon(self):
        xpath_x_icon = '//a[@aria-label="X"]'
        self._verify_visible(xpath_x_icon)

    def verify_title(self):
        xpath_title_page = '//h2[normalize-space()="OrangeHRM"]'
        self._verify_visible(xpath_title_page)