from playwright.sync_api import Page
class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def open(self, url: str):
        self.page.goto(url)

    def fill(self, locator: str, value: str):
        self.page.locator(locator).wait_for(state="visible")
        self.page.fill(locator, value)

    def click(self, locator: str):
        self.page.locator(locator).wait_for(state="visible")
        self.page.click(locator)