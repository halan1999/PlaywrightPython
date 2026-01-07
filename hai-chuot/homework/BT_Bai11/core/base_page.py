from playwright.sync_api import Page, Locator, expect

class BasePage:
    def __init__(self, page : Page):
        self.page = page 

    def _navigate_url(self, url : str):
        self.page.goto(url, wait_until = 'domcontentloaded')

    def _click(self, locator : Locator):
        locator.click()

    def _set_text(self, locator : Locator, value : str):
        locator.fill(value)

    def _verify_element_visible(self, locator : Locator):
        expect(locator).to_be_visible()