from playwright.sync_api import Page
from core.base_page import BasePage
from core.common_locators import CommonLocators

class HeaderComponents(BasePage):
    HEADER_LOGO = "//div[@class='header-wrapper']//a[contains(@href, 'desk')]"
    HEADER_ACCOUNT_SETTING_ICON = CommonLocators._attribute_data_original_title_xpath("a", "Account Settings")
    HEADER_APPS_ICON = CommonLocators._attribute_data_original_title_xpath("span", "Apps")
    HEADER_SYSTEM_CALENDAR_ICON = CommonLocators._attribute_data_original_title_xpath("a", "System Calendar")
    HEADER_SYSTEM_REPORT_ICON = CommonLocators._attribute_data_original_title_xpath("a", "System Reports")
    HEADER_CHOOSE_LANGUAGE_ICON = "//div[@class='ml-auto']//li[1]"
    HEADER_TODO_LIST_ICON = CommonLocators._attribute_data_original_title_xpath("a", "Todo List")
    HEADER_AVATAR_ICON = "//div[@class='ml-auto']//li[3]"
    HEADER_MY_ACCOUNT_BUTTON = CommonLocators._contains_text_xpath("span", "My Account")
    HEADER_LOGOUT_BUTTON = CommonLocators._contains_text_xpath("span", "Logout")
     
    def __init__(self, page):
        super().__init__(page)
        self.page = page
        

    def _logout(self):
        self._click(self.HEADER_AVATAR_ICON)
        self._take_screenshot("logout button form avatar display")
        self._click(self.HEADER_LOGOUT_BUTTON)
        self._take_screenshot("should be logout")
        self._expect_to_have_url("/login")

    def _click_and_take_screenshot_all_button_in_header(self):
        list_header_buttons = [
            (self.HEADER_AVATAR_ICON, "header avatar"),
            (self.HEADER_LOGO, "header logo"),
            (self.HEADER_ACCOUNT_SETTING_ICON, "header account setting"),
            (self.HEADER_APPS_ICON, "header app icon"),
            (self.HEADER_SYSTEM_CALENDAR_ICON, "header system calendar"),
            (self.HEADER_SYSTEM_REPORT_ICON, "header system report"),
            (self.HEADER_CHOOSE_LANGUAGE_ICON, "header choose language"),
            (self.HEADER_TODO_LIST_ICON, "header todo list")
        ]
        for locator, title in list_header_buttons:
            self._click(locator)
            self._take_screenshot(title)
            self.page.wait_for_timeout(300)
    
    