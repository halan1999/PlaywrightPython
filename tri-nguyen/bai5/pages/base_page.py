from playwright.sync_api import expect, Page, Locator, TimeoutError
import time, re

class BasePage:
    def __init__(self, page : Page):
        self.page = page

    def _navigate_to_page(self, url: str):
        self.page.goto(url, wait_until="domcontentloaded")

    def _get_locator(self, locator: str) -> Locator:
        return self.page.locator(locator)
    
    def _click_on_object(self, locator: str, name: str = ""):
        try:
            print(f"[Click] {name or locator}")
            self._get_locator(locator).click()
        except TimeoutError:
            print(f"[Lỗi] không thể click vào locator này")
            raise

    def _hover_on_object(self, locator: str):
        self._get_locator(locator).hover()
    
    def _fill_data(self, locator: str, text: str, name: str = ""):
        print(f"[Fill] '{text}' vào {name or locator}")
        self._get_locator(locator).fill(text)

    def _assert_text_visible(self, locator: str, text: str):
        print(f"[Assert] kiểm tra '{text}' hiển thị")
        expect(self._get_locator(locator)).to_contain_text(text)
        