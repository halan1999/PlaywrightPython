from playwright.sync_api import Page, expect, Locator, TimeoutError
import time

class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def _visit(self, url: str):
        print(f"[BasePage] Truy cập: {url}")
        self.page.goto(url, wait_until="domcontentloaded")

    def _get_locator(self, locator: str) -> Locator:
        return self.page.locator(locator)

    def _click(self, locator: str, name: str = ""):
        try:
            print(f"[Click] {name or locator}")
            self._get_locator(locator).click()
        except TimeoutError as e:
            print(f"[Lỗi] Không thể click vào {locator}")
            raise

    def _fill(self, locator: str, text: str, name: str = ""):
        print(f"[Fill] '{text}' vào {name or locator}")
        self._get_locator(locator).fill(text)

    def _assert_text_visible(self, locator: str, text: str):
        print(f"[Assert] Kiểm tra '{text}' hiển thị")
        expect(self._get_locator(locator)).to_contain_text(text)

    def _take_screenshot(self, filename: str):
        path = f"screenshots/{filename}_{int(time.time())}.png"
        self.page.screenshot(path=path)
        print(f"[SCREENSHOT] Lưu tại: {path}")