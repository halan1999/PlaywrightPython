from playwright.sync_api import Page
from core.base_page import BasePage
from core.common_locators import CommonLocators

class HeaderComponents(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.page = page
        self.header_logo_locator = "//div[@class='header-wrapper']//a[contains(@href, 'desk')]"
        self.header_account_setting_icon = CommonLocators._attribute_data_original_title_xpath("a", "Account Settings")
        self.header_apps_icon = CommonLocators._attribute_data_original_title_xpath("span", "Apps")
        self.header_system_calendar_icon = CommonLocators._attribute_data_original_title_xpath("a", "System Calendar")
        self.header_system_report_icon = CommonLocators._attribute_data_original_title_xpath("a", "System Reports")
        self.header_choose_language_icon = "//div[@class='ml-auto']//li[1]"
        self.header_todo_list_icon = CommonLocators._attribute_data_original_title_xpath("a", "Todo List")
        self.header_avatar_icon = "//div[@class='ml-auto']//li[3]"
        self.header_my_account_button = CommonLocators._contains_text_xpath("span", "My Account")
        self.header_logout_button = CommonLocators._contains_text_xpath("span", "Logout")

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
    
    