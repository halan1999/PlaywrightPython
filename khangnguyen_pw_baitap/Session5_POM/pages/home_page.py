from playwright.sync_api import Page, expect

class HomePage:
    def __init__(self, page: Page):
        self.page = page
        self._profile_link = "//a[contains(@href,'my-profile')]//p"

    def is_loaded(self):
        expect(self.page.locator(self._profile_link)).to_be_visible(timeout=10000)
        return True
