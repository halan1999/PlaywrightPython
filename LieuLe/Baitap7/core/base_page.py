import os
from playwright.sync_api import Page

class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def _visit(self, url: str):
        self.page.goto(url)

    def _click(self, locator):
        self.page.locator(locator).click()

    def _fill(self, locator: str, value: str):
        self.page.locator(locator).fill(value)

    def wait(self, seconds=1):
        self.page.wait_for_timeout(seconds * 1000)

    def screenshot(self, file_path: str):
        folder = os.path.dirname(file_path)
        os.makedirs(folder, exist_ok=True)

        self.page.screenshot(path=file_path, full_page=True)
        print("Saved:", os.path.abspath(file_path))
    
    