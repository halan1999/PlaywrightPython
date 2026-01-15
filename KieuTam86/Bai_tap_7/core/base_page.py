from playwright.sync_api import Page, expect, Locator
import time

class BasePage:
    """Lớp cha chứa các hành động Playwright cơ bản, kế thừa cho mọi Page Object."""
    def __init__(self, page: Page):
        self.page = page

    def _open_page(self, url: str):
        """Navigate to URL ..."""
        print(f"[BasePage] truy cập {url}")
        self.page.goto(url, wait_until="domcontentloaded")

    def _get_locator(self, locator: str) -> Locator:
        """Get locator of Object """
        return self.page.locator(locator)

    def _click(self, locator: str):
        """Thực hiện click với xử lý lỗi và ghi log."""
        try:
            print(f"[Click] {locator}")
            self.page.locator(locator).click()
        except TimeoutError as e:
            print(f"[Error] Cannot click on {locator} due to {e}")
            raise

    def _fill(self, locator: str, value: str):
        """Fill value on textbox input."""
        print(f"Fill value {value} vào {locator}")
        self.page.locator(locator).fill(value)

    def _verify_text(self, locator: str, text: str):
        """Kiểm tra văn bản mong đợi hiển thị trên giao diện."""
        expect(self.page.locator(locator)).to_contain_text(text)

    # def _return_count(self, locator: str) -> int:
    #     """Kiểm tra số lượng mong đợi hiển thị trên giao diện."""
    #     count_items = self.page.locator(locator).inner_text().strip()
    #     try:
    #         return int(count_items)
    #     except ValueError:
    #         print(f"Cannot change {count_items} to number")
    #         return

    def _select_menu(self, text: str):
        locator = "//li//a//span[normalize-space()={text}]"
        self._click(locator)    
        
    def _take_screenshot(self, filename: str):
        """Lưu ảnh chụp màn hình (sử dụng khi test Pass/fail)."""
        path_file = f"screenshots/{filename}_{int(time.time())}.png"
        self.page.screenshot(path=path_file)
        print(f"[SCREENSHOT] Lưu tại: {path_file}")    

    def _verify_value_visible(self, locator: str, text: str):
        """Kiểm tra vị trí có tồn tại trên form."""
        expect(self.page.locator(locator)).to_be_visible()
        print(f"[ASSERT]{locator} hiển thị thành công!")
    