from playwright.sync_api import expect
from core.base_component import BaseComponent
import time
from enum import Enum

class XpathHeader(Enum):
    ACCOUNT_SETTING = '//a[@data-original-title="Account Settings"]'    
    SYSTEM_CALENDAR = '//a[@data-original-title="System Calendar"]'
    SYSTEM_REPORT = '//a[@data-original-title="System Reports"]'
    PROFILE_ACCOUNT = '//img[@class="user-avtar"]'
    APPS = '//span[@data-original-title="Apps"]/parent::a'

class HeaderComponent(BaseComponent):
    def click_header(self, xpath_header : XpathHeader):
        self._click(xpath_header)

    def click_dropdown_menu(self, xpath_header : XpathHeader, label_dropdown_item : str):
        xpath_dropdown_item = f'// div[contains(@class,"dropdown-menu")]//span[normalize-space()="{label_dropdown_item}"]/parent::a'
        self._click(xpath_header, xpath_dropdown_item)