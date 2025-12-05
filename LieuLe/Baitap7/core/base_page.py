from playwright.sync_api import Page, expect, Locator, TimeoutError
import os

class BasePage:
    def __init__(self, page:Page):
        self.page = page

    def _visit(self, url: str):
        #print(f"[BasePage] Launch to: {url}")
        #self.page.goto(url, wait_until="domcontentloaded")
        print(f"[BasePage] Launch to: {url}")
        self.page.goto(url, wait_until="networkidle", timeout=60000)

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
        folder = os.path.join("LieuLe", "Baitap6", "screenshots")
        os.makedirs(folder, exist_ok=True)
        path = os.path.join(folder, filename)
        self.page.screenshot(path=path)
        print(f"[SCREENSHOT] Save at: {path}")
    
    def take_before_scroll_screenshot(self, selector, file_name):
        menu = self.page.locator(selector)
        folder = os.path.join("LieuLe", "Baitap6", "screenshots")
        os.makedirs(os.path.dirname(folder), exist_ok=True)
        menu.screenshot(path=file_name)

    def take_after_scroll_screenshot(self, selector, file_name):
            menu = self.page.locator(selector)
            self.page.evaluate("""(menu) => {
                 menu.scrollTo(0, menu.scrollHeight);
            }""",
            menu.element_handle())
            self.page.wait_for_timeout(1000)
            folder = os.path.join("LieuLe", "Baitap6", "screenshots")
            os.makedirs(folder, exist_ok=True)
            path = os.path.join(folder, file_name)
            menu.screenshot(path=path)
