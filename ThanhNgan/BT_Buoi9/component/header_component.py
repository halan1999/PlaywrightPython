from playwright.sync_api import Page
from core.base_page import BasePage
import time
from enum import Enum

class XpathHeader(Enum):
    HEADING = "//h6"
    UPGRADE_BUTTON = "//button[normalize-space()='Upgrade']"
    ICON_PROFILE = "(//img[@alt='profile picture'])[1]"
    LOGOUT_BUTTON = "//a[normalize-space()='Logout']"

class HeaderComponent(BasePage):
    def __init__(self, page):
        super().__init__(page)
    def logout(self,expath_header=XpathHeader):
        self._click(expath_header.ICON_PROFILE.value)
        self._click(expath_header.LOGOUT_BUTTON.value)
 