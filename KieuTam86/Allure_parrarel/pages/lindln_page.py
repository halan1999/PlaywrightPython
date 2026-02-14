from core.base_page import BasePage, expect
from playwright.sync_api import Playwright
import time


class LindlnPage(BasePage):

    HEADING = "h1"
    TITLE = "OrangeHRM"
    URL = "https://www.linkedin.com/company/orangehrm/"

    def __init__(self, page):
        super().__init__(page)

    def get_header_text(self) -> str:
        return self._get_text(self.HEADING)
    
    def verify_url_is_lindln(self):
        expect(self.page).to_have_url(self.URL)

    def verify_title_lindln(self):
        expect(self.page.locator(self.HEADING)).to_have_text(self.TITLE)
    
