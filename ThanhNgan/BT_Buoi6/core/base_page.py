from playwright.sync_api import Page, expect, Locator, TimeoutError
import time
class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def _goto(self, url: str):
        print(f"Truy cập đến: {url}")
        self.page.goto(url, wait_until="domcontentloaded")

    def _get_locator(self, locator: str):
        return self.page.locator(locator)
    
    def _click(self, locator: str):
        try:
            element = self.page.locator(locator)
            element.wait_for(state = "visible", timeout=5000)
            print(f"Click {locator}")
            element.click()
        except TimeoutError:
            print(f"Lỗi Element {locator} không hiển thị")
            print("element:",element)
            self._take_screenshot(f"error_click_{element}.png")
            raise
    
    def _fill(self, locator: str, text: str):
        print(f"Fill {text} vào {locator}")
        self._get_locator(locator).fill(text)

    def _assert_text_visible(self, locator: str, text: str):
        print(f"Assert Kiểm tra '{text}' hiển thị")
        expect(self._get_locator(locator)).to_contain_text(text)

    def _take_screenshot(self, filename: str):
        path = f"./BT_Buoi6/screenshots/{filename}_{time.time()}.png"
        self.page.screenshot(path=path)
        print(f"[SCREENSHOT] Lưu tại: {path}")
    
    

        
    
        