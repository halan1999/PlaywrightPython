from playwright.sync_api import Page
from core.base_page import BasePage
import time

class HeaderComponent(BasePage):

    header_items = [
            "//header//a[@data-original-title='Account Settings']",
            "//header//span[@data-original-title='Apps']",
            "//header//a[@data-original-title='System Calendar']",
            "//header//a[@data-original-title='System Reports']",
            "//header//a[@data-toggle='dropdown']//img[contains(@src,'languages_flag')]",
            "//header//a[@data-original-title='Todo List']"
        ]
    icon_profife = "//img[@class='user-avtar']"
    btn_logout = "//span[normalize-space()='Logout']"
    
    def __init__(self, page):
        super().__init__(page)
        
    def click_all_items(self):
        for index, item in enumerate(self.header_items):
            self._click(item)
            time.sleep(1)
            self._take_screenshot(filename=f"header_{index + 1}")

    def logout(self):
        self._click(self.icon_profife)
        self._click(self.btn_logout)
 