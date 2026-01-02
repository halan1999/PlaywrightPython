from playwright.sync_api import Page
from core.base_page import BasePage
import time
from enum import Enum

class MenuComponent(BasePage):

    class XpathMenu(Enum):
        SEARCH = "//input[@placeholder='Search']"
        MENU = "//ul[@class='oxd-main-menu']/li"
        ADMIN = f"({MENU})[1]"
        PIM = f"({MENU})[2]"
        LEAVE = f"({MENU})[3]"
        TIME = f"({MENU})[4]"
        RECRUITMENT = f"({MENU})[5]"
        MY_INFO = f"({MENU})[6]" 
        PERFORMANCE = f"({MENU})[7]"
        DASHBOARD = f"({MENU})[8]"
        DIRECTORY = f"({MENU})[9]"
        MAINTENANCE = f"({MENU})[10]"
        CLAIM = f"({MENU})[11]"
        BUZZ = f"({MENU})[12]"

    def __init__(self, page):
        super().__init__(page)

    def search(self, text: str, expath_menu=XpathMenu):
        self._fill(expath_menu.SEARCH.value, text)
 