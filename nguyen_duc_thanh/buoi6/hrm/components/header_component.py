import time
from buoi6.hrm.pages.base_page import BasePage


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

    # def click_to_account_setting(self):
    #     self.click_element(self.APPS)
           
    # def click_to_apps(self):
    #     self.click_element(self.ACCOUNT_SETTING)

    # def click_to_system_calender(self):
    #     self.click_element(self.SYSTEM_CALENDER)

    # def click_to_system_report(self):
    #     self.click_element(self.SYSTEM_REPORT)

    # def click_to_languague(self):
    #     self.click_element(self.LANGUAGUE)
        

    def click_to_logout(self):
        self.click_element(self.USERNAME)
        self.click_element(self.LOGOUT)


    