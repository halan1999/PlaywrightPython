from playwright.sync_api import Page, expect, Locator, TimeoutError
import time

class BasePage:
    def __init__(self, page: Page):
        self.page=page

    def _goto(self, url: str):
        self.page.goto(url, wait_until="domcontentloaded")

    def _get_locator(self, locator: str) -> Locator:
        return self.page.locator(locator)

    def _fill(self, locator: str, text: str):
        self.page.locator(locator).fill(text)

    def _click(self, locator: str):
        self.page.locator(locator).click()

    def _assert_text_visible(self, locator: str):
        expect(self.page.locator(locator)).to_be_visibile()
    
    def _take_screenshot(self, filename: str):
        path = f"screenshots/{filename}_{int(time.time())}.png"
        self.page.screenshot(path=path)