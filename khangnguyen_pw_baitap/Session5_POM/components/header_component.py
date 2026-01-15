from playwright.sync_api import Page
from pages.base_page import BasePage
import re, time, os

class HeaderComponent(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.page = page

        # Header locators
        self._account_settings_icon = page.locator('//div[@class="header-wrapper"]//a[contains(@data-original-title,"Account Settings")]')
        self._apps_icon = page.locator('//div[@class="header-wrapper"]//span[contains(@data-original-title,"Apps")]')
        self._system_calendar_icon = page.locator('//div[@class="header-wrapper"]//a[contains(@data-original-title,"System Calendar")]')
        self._system_reports_icon = page.locator('//div[@class="header-wrapper"]//a[contains(@data-original-title,"System Reports")]')
        self._user_profile = page.locator('//img[contains(@src,"user")]/parent::a[contains(@class,"dropdown")]')
        
        self.header_icons = [
            self._account_settings_icon,
            self._apps_icon,
            self._system_calendar_icon,
            self._system_reports_icon,
        ]

        # User profile dropdown locators
        self._user_profile_dropdown = page.locator('//div[@class=" dropdown-header"]/parent::div[contains(@class,"dropdown")]')
        self._logout_dropdown_item = page.locator('//div[contains(@class,"dropdown")]//a[contains(@href,"system-logout")]')

    def _logout(self):
        self._user_profile.click()
        self._logout_dropdown_item.click()
        
    def click_header_icons(self):
        os.makedirs("screenshots", exist_ok=True)
        for header_icon in self.header_icons:
            try:
                locator_name = [k for k, v in self.__dict__.items() if v == header_icon]
                name = locator_name[0] if locator_name else "unknown_icon"

                header_icon.click()

                screenshot_path = f"screenshots/screenshot_{name}.png"
                self.take_screenshot(screenshot_path)

                print(f"[INFO] Clicked and captured {screenshot_path}")
            except Exception as e:
                print(f"[ERROR] Failed to click {name}: {e}")
        


    

