from playwright.sync_api import Page
import os

class BasePage:
    def __init__(self, page):
        self.page = page

    def click(self, locator):
        self.page.locator(locator).click()

    def fill(self, locator, text):
        self.page.locator(locator).fill(text)

    def get_text(self, locator):
        return self.page.locator(locator).inner_text()

    def take_screenshot(self, file_path): 
        self.page.screenshot(path=file_path)
 
    def is_visible(self, locator):
        return self.page.locator(locator).is_visible()

    def hover(self, locator):
        self.page.locator(locator).hover()
