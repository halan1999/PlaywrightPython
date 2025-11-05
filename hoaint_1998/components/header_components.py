from playwright.sync_api import Page
from pages.base_page import BasePage
from locators.base_component import BaseComponent

class HeaderComponents(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.page = page
        self.header_logo_locator = BaseComponent.HEADER_LOGO
        self.header_account_setting_icon = BaseComponent.HEADER_ACCOUNT_SETTING_ICON
        self.header_apps_icon = BaseComponent.HEADER_APPS_ICON
        self.header_system_calendar_icon = BaseComponent.HEADER_SYSTEM_CALENDAR
        self.header_system_report_icon = BaseComponent.HEADER_SYSTEM_REPORTS
        self.header_choose_language_icon = BaseComponent.HEADER_CHOOSE_LANGUAGE_ICON
        self.header_todo_list_icon = BaseComponent.HEADER_TODO_LIST_ICON
        self.header_avatar_icon = BaseComponent.HEADER_AVATAR_ICON
        self.header_my_account_button = BaseComponent.HEADER_MY_ACCOUNT_BUTTON
        self.header_logout_button = BaseComponent.HEADER_LOGOUT_BUTTON

    def _logout(self):
        self._click(self.header_avatar_icon)
        self._take_screenshot("logout button form avatar display")
        self._click(self.header_logout_button)
        self._take_screenshot("should be logout")
        self._expect_to_have_url("/login")

    def _click_and_take_screenshot_all_button_in_header(self):
        list_header_buttons = [
            (self.header_avatar_icon, "header avatar"),
            (self.header_logo_locator, "header logo"),
            (self.header_account_setting_icon, "header account setting"),
            (self.header_apps_icon, "header app icon"),
            (self.header_system_calendar_icon, "header system calendar"),
            (self.header_system_report_icon, "header system report"),
            (self.header_choose_language_icon, "header choose language"),
            (self.header_todo_list_icon, "header todo list")
        ]
        for locator, title in list_header_buttons:
            self._click(locator)
            self._take_screenshot(title)
            self.page.wait_for_timeout(300)
    
    