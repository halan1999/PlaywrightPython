from playwright.sync_api import Page, expect, Locator, TimeoutError

class BasePage:
    def __init__(self, page):
        self.page = page

    def _visit(self, url: str):
        print(f"[BasePage] Launch to: {url}")
        self.page.goto(url, wait_until="domcontentloaded")

    def _get_locator(self, locator:str) -> Locator:
        return self.page.locator(locator)
    
    def _click(self, locator: str):
        self._get_locator(locator).click()
        
    def _fill(self, locator: str, text: str):
        self._get_locator(locator).fill(text)

    