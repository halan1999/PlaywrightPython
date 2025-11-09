from playwright.sync_api import Page
import os

class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def click(self, locator: str):
        self.page.locator(locator).click()

    def fill(self, locator: str, value: str):
        self.page.locator(locator).fill(value)

    def goto(self, url: str):
        self.page.goto(url)

    def take_screenshot(self, filename: str):
        os.makedirs("screenshots", exist_ok=True)
        self.page.screenshot(path=filename)