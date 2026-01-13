from playwright.sync_api import Page
from playwright.sync_api import TimeoutError as PlaywrightTimeoutError
import allure

class BasePage:
    def __init__(self, page: Page):
        self.page = page
    
    def _visit(self, url, wait_selector=None):
        with allure.step(f"Navigate to {url}"):
            try:
                self.page.goto(url, timeout=60000)

                if wait_selector:
                    self.page.wait_for_selector(
                        wait_selector,
                        timeout=30000
                    )

            except PlaywrightTimeoutError:
                screenshot = self.page.screenshot(full_page=True)
                allure.attach(
                    screenshot,
                    name="Navigation failed",
                    attachment_type=allure.attachment_type.PNG
                )
                raise

    def click(self, xpath: str):
        self.page.locator(xpath).click()

    def fill(self, xpath: str, value: str):
        self.page.locator(xpath).fill(value)

    def get_locators(self, xpath: str):
        return self.page.locator(xpath)

    def screenshot(self, path: str):
        self.page.screenshot(path=path, full_page=True)

    