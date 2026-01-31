from playwright.sync_api import Page, expect, Locator, TimeoutError

class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def _visit(self, url: str):
        print(f"[BasePage] Truy cập: {url}")
        self.page.goto(url, wait_until="domcontentloaded")

    def _get_locator(self, locator: str) -> Locator:
        return self.page.locator(locator)

    def _click(self, locator: str, name: str = ""):
        print(f"[Click] {name or locator}")
        self._get_locator(locator).click()

    def _fill(self, locator: str, text: str, name: str = ""):
        print(f"[Fill] '{text}' vào {name or locator}")
        self._get_locator(locator).fill(text)

    def _get_text(self, locator: str):
        return self.page.locator(locator).inner_text()

    def _assert_text_visible(self, locator: str, text: str):
        print(f"[Assert] Kiểm tra '{text}' hiển thị")
        expect(self._get_locator(locator)).to_contain_text(text)

    def _take_screenshot(self, filename: str):
        path = f"BT_BUOI12/screenshots/{filename}"
        self.page.screenshot(path=path)
        print(f"[SCREENSHOT] Lưu tại: {path}")

    def _bring_to_front(self):
        self.page.bring_to_front()

    def _click_and_wait_for_new_page(self, locator: str, name: str = "", timeout: int = 15000):
        """
        Click vào locator → mở tab mới → return Page mới.
        """
        print(f"[MultiTab]: Click '{name}' và chờ tab mới mở...")

        with self.page.context.expect_page(timeout=timeout) as new_page_info:
            self.page.locator(locator).click()

        new_page = new_page_info.value
        new_page.wait_for_load_state("load")

        print(f"[MultiTab]: Tab mới URL = {new_page.url}")
        return new_page
