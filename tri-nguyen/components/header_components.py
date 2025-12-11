from core.base_component import BaseHeaderComponent
from core.base_page import BasePage
from playwright.sync_api import expect
import re, time

class HeaderComponent(BasePage, BaseHeaderComponent):
    account_profile = "//header//a//img[@class='user-avtar']"
    Btn_MyAccount = "//span[normalize-space()='My Account']/parent::a"
    Btn_loggout = "//span[normalize-space()='Logout']"
    def __init__(self, page):
        super().__init__(page)
        self.header = BaseHeaderComponent(page)

    def test_loggout(self):
        self._click_on_object(self.account_profile)
        self._click_on_object(self.Btn_loggout)

    def test_click_icon_logo_header(self):
        self.header.logo_header.click()
        self._take_screenshots("click_header_logo.png")

    def test_click_icon_account_setting(self):
        self.header.account_setting.click()
        self._take_screenshots("click_header_account_setting.png")

    def test_click_icon_apps(self):
        self.header.apps.click()
        self._take_screenshots("click_apps_icon.png")
    
    def test_click_icon_system_calendar(self):
        self.header.system_calendar.click()
        self._take_screenshots("click_system_calendar.png")

    def test_click_icon_system_report(self):
        self.header.system_report.click()
        self._take_screenshots("click_system_report.png")

    def test_click_language_icon(self):
        self.header.language_icon.click()
        time.sleep(3)
        self._take_screenshots("click_language_icon.png")

    def test_click_todo_list(self):
        self.header.todo_list.click()
        self._take_screenshots("click_todo_icon.png")