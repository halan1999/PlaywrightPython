import os
from pages.base_page import BasePage

class HeaderComponent(BasePage):
    def __init__(self, page):
        super().__init__(page)

        # Header locators
        self.account_settings = '//a[contains(@data-original-title,"Account Settings")]'
        self.apps = '//span[contains(@data-original-title,"Apps")]'
        self.system_calendar = '//a[contains(@data-original-title,"System Calendar")]'
        self.system_reports = '//a[contains(@data-original-title,"System Reports")]'

        self.header_items = [
            ("account_settings", self.account_settings),
            ("apps", self.apps),
            ("system_calendar", self.system_calendar),
            ("system_reports", self.system_reports),
        ]

    def click_header_items_and_take_screenshot(self):
        os.makedirs("screenshots", exist_ok=True)
        for name, locator in self.header_items:
            self.click(locator)

            file_path = f"screenshots/screenshot_{name}.png"

            self.take_screenshot(file_path)
            print(f"[INFO] Clicked and took screenshot: {file_path}")
