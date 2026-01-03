from playwright.sync_api import Page

class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def click(self, xpath: str):
        self.page.locator(xpath).click()

    def fill(self, xpath: str, value: str):
        self.page.locator(xpath).fill(value)

    def get_locators(self, xpath: str):
        return self.page.locator(xpath)

    def screenshot(self, path: str):
        self.page.screenshot(path=path, full_page=True)
