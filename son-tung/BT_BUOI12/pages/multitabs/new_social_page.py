from playwright.sync_api import expect
from BT_BUOI12.core.base_page import BasePage

class NewPage(BasePage):
    icon_twitter = "//h1//a//div"

    def __init__(self, page):
        super().__init__(page)

    def get_heading_text(self, heading) -> str:
        return self._get_text(f"//h1[contains(normalize-space(), '{heading}')]")

    def verify_element(self):
        expect(self.page.locator(self.icon_twitter)).to_be_visible()