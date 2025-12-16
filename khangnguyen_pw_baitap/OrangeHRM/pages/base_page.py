import os
from playwright.sync_api import expect


class BasePage:
    def __init__(self, page):
        self.page = page

    def click(self, locator):
        self.page.locator(locator).click()

    def fill(self, locator, value):
        self.page.locator(locator).fill(value)

    def expect_visible(self, locator):
        expect(self.page.locator(locator)).to_be_visible()

    def bring_to_front(self):
        self.page.bring_to_front()

    def take_screenshot(self, path, full_page=True):
        os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
        self.page.screenshot(path=path, full_page=full_page)
        return path
