from core.base_page import BasePage
from playwright.sync_api import Page, expect, Locator, TimeoutError
import time

class HeaderComponent(BasePage):
    header_items=[
        "//header//a[@data-original-title='Account Settings']",
        "//header//span[@data-original-title='Apps']",
        "//header//a[@data-original-title='System Calendar']",
        "//header//a[@data-original-title='System Reports']",
        "//header//li[1]//a[@data-toggle='dropdown']",
        "//a[@class='pc-head-link mr-0']//*[name()='svg']"
    ]

    menu_items=[
        "//span[normalize-space()='Attendance']",
        "//span[normalize-space()='Projects']",
        "//span[normalize-space()='Tasks']",
        "//span[normalize-space()='Payroll']",
        "//a[normalize-space()='Requests']",
        "//span[normalize-space()='Helpdesk']",
        "//span[normalize-space()='Training Sessions']",
        "//span[normalize-space()='Employees']",
        "//span[normalize-space()='Recruitment (ATS)']",
        "//a[normalize-space()='Core HR']",
        "//span[normalize-space()='Finance']",
        "//a[normalize-space()='Performance (PMS)']",
        "//span[normalize-space()='Inventory Control']",
        "//span[normalize-space()='Manage Clients']",
        "//span[normalize-space()='Leads']",
        "//span[normalize-space()='Invoices']",
        "//span[normalize-space()='Estimates']",
        "//span[normalize-space()='Disciplinary Cases']"
    ]

    logout_button="//span[normalize-space()='Logout']"
    profile_icon="//img[@class='user-avtar']"

    def click_all_header_items(self):
        for index, item in enumerate(self.header_items,start=1):
            self._click(item)
            self._take_screenshot(f"header_item_{index}")

    def click_all_menu_items(self):
        for index, item in enumerate(self.menu_items,start=1):
            menu_locator = self.page.locator("//nav[@class='pc-sidebar light-sidebar']")
            menu_locator.evaluate("el => el.scrollTop = el.scrollHeight") 
            self._click(item)
            time.sleep(3)
            self._take_screenshot(f"menu_item_{index}")

    def logout(self):
        self._click(self.profile_icon)
        self._click(self.logout_button)