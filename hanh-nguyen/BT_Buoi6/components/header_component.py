from playwright.sync_api import Page
from core.base_page import BasePage

class HeaderComponent(BasePage):
    HEADER_LOGO = "//div[@class='pcm-logo']//img"
    ACCOUNT_SETTING = "//a[contains(@data-original-title, 'Account Settings')]"
    APPS_SETTING = "//span[contains(@data-original-title, 'Apps')]/parent::a"
    SYSTEM_CALENDAR_SETTING = "//a[contains(@data-original-title, 'System Calendar')]"
    SYSTEM_REPORT_SETTING = "//a[contains(@data-original-title, 'System Reports')]"
    COUNTRY_SELECTOR = "//img[@src='https://hrm.anhtester.com/public/uploads/languages_flag/en.gif']//parent::a[@data-toggle='dropdown']"
    TODO_LIST = "//a[contains(@data-original-title, 'Todo List')]"
    USER_ACCOUNT = "//img[@src='https://hrm.anhtester.com/public/uploads/users/thumb/photo_2025-05-23_16-03-51 (2).jpg']//parent::a"
    
    def click_logo(self):
        self._click(self.HEADER_LOGO)

    def click_account_setting(self):
        self._click(self.ACCOUNT_SETTING)

    def click_app_settings(self):
        self._click(self.APPS_SETTING)

    def click_system_calendar(self):
        self._click(self.SYSTEM_CALENDAR_SETTING)

    def click_system_report(self):
        self._click(self.SYSTEM_REPORT_SETTING)

    def click_country_selector(self):
        self._click(self.COUNTRY_SELECTOR)

    def click_todo_list(self):
        self._click(self.TODO_LIST)

    def click_user_account(self):
        self._click(self.USER_ACCOUNT)