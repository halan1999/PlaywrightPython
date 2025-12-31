import os
import re
from playwright.sync_api import Page, expect
from pages.base_page import BasePage


class AccountSettingsPage(BasePage):
    # Locators
    _upload_file_field = '//input[@name="file"]'
    _update_picture_btn = 'button:has-text("Update Picture")'

    def __init__(self, page: Page):
        super().__init__(page)

    # Click tab menu on Account Settings page by menu name
    def click_tab(self, menu_name: str):
        tab = self.page.get_by_role("tab", name=menu_name)
        tab.wait_for(state="visible", timeout=10000)
        tab.click()

    # Upload new avatar on Profile Picture section
    def upload_profile_picture(self, file_path: str):
        upload_input = self.page.locator(self._upload_file_field)
        upload_input.wait_for(state="attached", timeout=10000)
        upload_input.set_input_files(file_path)

    # Wait until the file is completely uploaded
    def wait_the_upload_is_completed(self, file_path: str):
        upload_input = self.page.locator(self._upload_file_field)
        upload_input.wait_for(state="attached", timeout=10000)

        file_name = os.path.basename(file_path)
        pattern = re.compile(rf".*{re.escape(file_name)}$")

        expect(upload_input).to_have_value(pattern, timeout=10000)

    # Click Update Picture buttohn
    def click_update_picture(self):
        btn = self.page.locator(self._update_picture_btn)
        expect(btn).to_be_visible(timeout=10000)
        expect(btn).to_be_enabled(timeout=10000)
        btn.click()
        self.reload_page()
