import os
from pages.base_page import BasePage


class HeaderComponent(BasePage):
    # Locators
    account_settings = '//a[contains(@data-original-title,"Account Settings")]'
    apps = '//span[contains(@data-original-title,"Apps")]'
    system_calendar = '//a[contains(@data-original-title,"System Calendar")]'
    system_reports = '//a[contains(@data-original-title,"System Reports")]'
    avatar_img = '//header//img[contains(@src,"users")]'

    def __init__(self, page):
        super().__init__(page)

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
            self.page.wait_for_timeout(300)

            file_path = f"screenshots/screenshot_{name}.png"
            self.take_screenshot(file_path)
            print(f"[INFO] Clicked and took screenshot: {file_path}")

    # Click each items on the page header and take a screenshot
    def click_header_items(self):
        self.click_header_items_and_take_screenshot()

    # Get the source of avatar
    def get_avatar_src(self, timeout=10000):
        avatar = self.page.locator(self.avatar_img)
        avatar.wait_for(state="visible", timeout=timeout)
        return avatar.get_attribute("src")

    # Verify the file name is contained in the source of avatar on the header
    def verify_avatar_src_contains(self, expected_file_name, timeout=10000):
        src = self.get_avatar_src(timeout=timeout)
        assert expected_file_name in src, (
            f"Expected '{expected_file_name}' in src, but got: {src}"
        )