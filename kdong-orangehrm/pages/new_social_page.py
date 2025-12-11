from core.base_page import BasePage
from playwright.sync_api import expect


class NewSocialPage(BasePage):
    # icon_twitter = "//h1//a//div"

    def __init__(self, page):
        super().__init__(page)

    def get_heading_text(self, heading) -> str:
        return self._get_text(f"//h1[contains(normalize-space(), '{heading}')]")

    def verify_element(self):
        expect(self.page.locator(self.icon_twitter)).to_be_visible()

    