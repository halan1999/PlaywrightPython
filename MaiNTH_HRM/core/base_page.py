from typing import Optional
from playwright.sync_api import Page, Locator, expect
import time

class BasePage:

    def __init__(self, page: Page):
        self.page = page

    def open(self, url: str):
        self.page.goto(url)

    def click(self, locator: str):
        self.page.click(locator)

    def fill(self, locator: str, value: str):
        self.page.fill(locator, value)

    def get_text(self, locator: str):
        """Return inner text of element."""
        return self.page.inner_text(locator)

    def is_visible(self, locator: str):
        """Return whether element is visible."""
        return self.page.is_visible(locator)

    def wait_for(self, locator: str, state: str = "visible"):
        """Wait for selector to reach a given state: 'visible', 'hidden', 'attached', 'detached'."""
        self.page.wait_for_selector(locator, state=state)

    def assert_text(self, locator: str, expected: str):
        """Assert element's text equals expected using Playwright expect."""
        expect(self.page.locator(locator)).to_have_text(expected)

    def assert_contains_text(self, locator: str, substring: str):
        """Assert element's text contains substring."""
        expect(self.page.locator(locator)).to_contain_text(substring)

    def assert_url_contains(self, part: str):
        """Assert current URL contains given substring."""
        expect(self.page).to_have_url(lambda url: part in url)

    def _take_screenshot(self, filename: str):
        """Lưu ảnh chụp màn hình (sử dụng khi test fail)."""
        path = f"screenshots/{filename}_{int(time.time())}.png"
        self.page.screenshot(path=path)
        print(f"[SCREENSHOT] Lưu tại: {path}")