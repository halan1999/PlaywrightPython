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
