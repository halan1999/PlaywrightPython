from playwright.sync_api import Page, expect, Locator, TimeoutError
import time,json

class BasePage:
    """Lớp cha chứa các hành động Playwright cơ bản, kế thừa cho mọi Page Object."""

    def __init__(self, page):
        self.page = page

    def _open_url(self, url):
        self.page.goto(url)

    def _get_locator(self, locator: str):
        print(f"[DEBUG] self.page type: {type(self.page)}")  # <--- thêm dòng này
        print(f"[DEBUG] locator: {locator}")
        return self.page.locator(locator)


    def _click(self, locator: str, name: str = ""):
        """Thực hiện click với xử lý lỗi và ghi log."""
        try:
            print(f"[Click] {name or locator}")
            self._get_locator(locator).click()
        except TimeoutError:
            print(f"[Lỗi] Không thể click vào {locator}")
            raise


    def _fill(self, locator: str, text: str, name: str = ""):
        """Điền dữ liệu vào ô input."""
        print(f"[Fill] '{text}' vào {name or locator}")
        self._get_locator(locator).fill(text)

    def _assert_text_visible(self, locator: str, text: str):
        """Kiểm tra văn bản mong đợi hiển thị trên giao diện."""
        print(f"[Assert] Kiểm tra '{text}' hiển thị")
        expect(self._get_locator(locator)).to_contain_text(text)

    def _take_screenshot(self, filename: str):
        """Lưu ảnh chụp màn hình (sử dụng khi test fail)."""
        path = f"screenshots/{filename}_{int(time.time())}.png"
        self.page.screenshot(path=path)
        print(f"[SCREENSHOT] Lưu tại: {path}")

    
