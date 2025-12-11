from playwright.sync_api import Page, expect

class BasePage:
    """Lớp cha chứa các hành động Playwright cơ bản, kế thừa cho mọi Page Object."""
    def __init__(self, page: Page):
        self.page = page

    def _open_page(self, url: str):
        """Điều hướng tới URL được chỉ định."""
        print(f"[BasePage] truy cập {url}")
        self.page.goto(url, wait_until="domcontentloaded")

    def _click(self, locator: str):
        """Thực hiện click với xử lý lỗi và ghi log."""
        try:
            print(f"[Click] {locator}")
            self.page.locator(locator).click()
        except TimeoutError:
            print(f"[Error] Cannot click on {locator}")
            raise

    def _fill(self, locator: str, value: str):
        """Điền dữ liệu vào ô input."""
        print(f"Fill value {value} vào {locator}")
        self.page.locator(locator).fill(value)

    def _verify_text(self, locator: str, text: str):
        """Kiểm tra văn bản mong đợi hiển thị trên giao diện."""
        expect(self.page.locator(locator)).to_contain_text(text)

    def _return_count(self, locator: str) -> int:
        """Kiểm tra số lượng mong đợi hiển thị trên giao diện."""
        count_items = self.page.locator(locator).inner_text().strip()
        try:
            return int(count_items)
        except ValueError:
            print(f"Cannot change {count_items} to number")
            return