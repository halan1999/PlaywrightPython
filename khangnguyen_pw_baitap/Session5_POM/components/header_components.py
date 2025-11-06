from playwright.sync_api import Page
from pages.base_page import BasePage
import re

class HeaderComponent(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.page = page

        # Header locators
        self._account_settings_icon = page.locator('//div[@class="header-wrapper"]//a[contains(@data-original-title,"Account Settings")]')
        self._apps_icon = page.locator('//div[@class="header-wrapper"]//span[contains(@data-original-title,"Apps")]')
        self._system_calendar_icon = page.locator('//div[@class="header-wrapper"]//a[contains(@data-original-title,"System Calendar")]')
        self._system_reports = page.locator('//div[@class="header-wrapper"]//a[contains(@data-original-title,"System Reports")]')
        self._user_profile = page.locator('//li[contains(@class,"dropdown")]//span[text()="admin_example"]')

        # User profile dropdown locators
        self._user_profile_dropdown = page.locator('//div[@class=" dropdown-header"]/parent::div[contains(@class,"dropdown")]')
        self._logout_dropdown_item = page.locator('//div[contains(@class,"dropdown")]//a[contains(@href,"system-logout")]')

    def _logout(self):
        self._user_profile.click()
        self._logout_dropdown_item.click()
        
    def _click_account_settings_icon(self):
        self._account_settings_icon.click()

    def _click__apps_icon(self):
        self._apps_icon.click()

    def _click__system_calendar_icon(self):
        self._system_calendar_icon.click()

    def _click__system_reports(self):
        self._system_reports.click()
        


    

