from playwright.sync_api import Page, expect, Locator, TimeoutError

class BasePage:
    """Lớp cha chứa các hành động Playwright cơ bản, kế thừa cho mọi Page Object."""
    
    def __init__(self, page: Page):
        self.page = page
        # self.SCREENSHOT_DIR = "screenshots"
        # os.makedirs(self.SCREENSHOT_DIR, exist_ok=True)

    def _visit(self, url: str):
        """Điều hướng tới URL được chỉ định."""
        print(f"[BasePage] Navigate to: {url}")
        self.page.goto(url, wait_until="domcontentloaded")
    
    def _get_page_url(self):
        return self.page.url

    def wait_for_element(self, locator: str, timeout: int = 5000, state: str = "visible"):
        """
        Chờ cho element xuất hiện, ẩn, hay biến mất.
        state = "visible" | "attached" | "hidden" | "detached"
        """
        print(f"[Wait for] {locator} ({state})")
        self.page.locator(locator).wait_for(state=state, timeout=timeout)

    def _open_new_tab(self, locator: str, name: str = "", timeout: int = 15000):
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
    
    def _get_page_url(self) -> str:
        """Lấy URL hiện tại của tab"""
        return self.page.url
    
    def _wait_for_element(self,locator:str,timeout:int=15000):
        self.wait_for_element(locator=locator,timeout=timeout)