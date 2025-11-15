import time
from buoi7.pages.base_page import BasePage


class HeaderComponent(BasePage):
    header_locator ={
    "//a[@data-original-title='Account Settings']//*[name()='svg']",
    "//a[@class='pc-head-link active dropdown-toggle arrow-none mr-0']",
    "//a[@href='https://hrm.anhtester.com/erp/system-calendar']",
    "//*[name()='path' and contains(@d,'M22 12A10 ')]",
    "(//li[@class='dropdown pc-h-item'])[2]",
    }
    LOGOUT = "//li[@class='dropdown pc-h-item show']//a[2]"
    USERNAME = "//span[@class='user-name']"

    def click_to_headers(self):
        for index, locator in enumerate(self.header_locator,start = 1):
            self.click_element(locator)
            time.sleep(3)
            self.take_screenshot(f"header_screenshot_{index}")

    def click_to_logout(self):
        self.click_element(self.USERNAME)
        self.click_element(self.LOGOUT)


    