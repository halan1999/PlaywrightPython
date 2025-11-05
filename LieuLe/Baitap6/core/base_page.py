from playwright.sync_api import Page, expect, Locator, TimeoutError

class BasePage:
    def __init__(self, page:Page):
        self.page = page

    def _visit(self, url: str):
        print(f"[BasePage] Launch to: {url}")
        self.page.goto(url, wait_until="domcontentloaded")

    def _get_locator(self, locator:str) -> Locator:
        return self.page.locator(locator)
    
    def _click(self, locator: str):
        try:
            print(f"[Click] {locator}")
            self._get_locator(locator).click()
        except TimeoutError:
            print(f"[Error] Can not click on {locator}")
            raise

    def _fill(self, locator: str, text: str):
        print(f"[Fill] '{text} into {locator}")
        self._get_locator(locator).fill(text)
    
    def _take_screenshot(self, filename: str):
        path = f"screenshots/{filename}"
        self.page.screenshot(path=path)
        print(f"[SCREENSHOT] Save at: {path}")