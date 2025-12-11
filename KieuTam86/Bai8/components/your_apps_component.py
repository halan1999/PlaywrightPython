from playwright.sync_api import Playwright
from core.base_page import BasePage

class YourApps(BasePage):
    your_apps_items = [
        "//span[@class='pc-mtext' and normalize-space()='Home']",
       "//span[@class='pc-mtext' and normalize-space()='Attendance']",
        "//span[@class='pc-mtext' and normalize-space()='Projects']",
        "//span[@class='pc-mtext' and normalize-space()='Tasks']",
        "//span[@class='pc-mtext' and normalize-space()='Payroll']",
        "//a[normalize-space()='Requests']",
        "//span[@class='pc-mtext' and normalize-space()='Helpdesk']",
        "//span[@class='pc-mtext' and normalize-space()='Training Sessions']"
    ]
    requests=[
        "//a[@class='pc-link' and normalize-space()='Leave Request']",
        "//a[@class='pc-link' and normalize-space()='Expense Claim']",
        "//a[@class='pc-link' and normalize-space()='Request Loan']",
        "//a[@class='pc-link' and normalize-space()='Travel Request']",
        "//a[@class='pc-link' and normalize-space()='Advance Salary']",
        "//a[@class='pc-link' and normalize-space()='Overtime Request']"
    ]
    your_company_items = [
        "//span[@class='pc-mtext' and normalize-space()='Employees']",
        "//span[@class='pc-mtext' and normalize-space()='Recruitment (ATS)']",
        "//a[@class='pc-link sidenav-toggle' and normalize-space()='Core HR']",
        "//span[@class='pc-mtext' and normalize-space()='Finance']",
        "//a[@class='pc-link sidenav-toggle' and normalize-space()='Performance (PMS)']",
        "//span[@class='pc-mtext' and normalize-space()='Inventory Control']",
        "//span[@class='pc-mtext' and normalize-space()='Manage Clients']",
        "//span[@class='pc-mtext' and normalize-space()='Leads']",
        "//span[@class='pc-mtext' and normalize-space()='Invoices']",
        "//span[@class='pc-mtext' and normalize-space()='Estimates']",
        "//span[@class='pc-mtext' and normalize-space()='Disciplinary Cases']"
    ]
    core_hr = [
        "//a[@class='pc-link' and normalize-space()='Department']",
        "//a[@class='pc-link' and normalize-space()='Designation']",
        "//a[@class='pc-link' and normalize-space()='Policies']",
        "//a[@class='pc-link' and normalize-space()='Make Announcement']",
        "//a[@class='pc-link' and normalize-space()='Organization Chart']"
    ]
    performance = [
        "//a[@class='pc-link' and normalize-space()='KPI (Indicator)']",
        "//a[@class='pc-link' and normalize-space()='KPA (Appraisal)']",
        "//a[@class='pc-link' and normalize-space()='Competencies']",
        "//a[@class='pc-link' and normalize-space()='Track Goals (OKRs)']",
        "//a[@class='pc-link' and normalize-space()='Goal Type']",
        "//a[@class='pc-link' and normalize-space()='Goals Calendar']"
    ]
    inventory_control = [
        "//a[@class='pc-link' and normalize-space()='Warehouses']",
        "//a[@href='#!' and normalize-space()='Products']",
        "//a[@class='pc-link' and normalize-space()='Suppliers']",
        "//a[@href='#!' and normalize-space()='Purchases']",
        "//a[@href='#!' and normalize-space()='Sales Order']"
    ]
    products = [
        "//a[@href='https://hrm.anhtester.com/erp/product-list' and normalize-space()='Products']",
        "//a[@class='pc-link' and normalize-space()='Out of Stock']",
        "//a[@class='pc-link' and normalize-space()='Expired Products']",
        "//a[@class='pc-link' and normalize-space()='Product Tax']",
        "//a[@class='pc-link' and normalize-space()='Product Category']"
    ]
    purchases = [
        "//a[@class='pc-link' and normalize-space()='New Purchase']",
        "//a[@class='pc-link' and normalize-space()='Purchase List']"
    ]
    sale_order =[
        "//a[@class='pc-link' and normalize-space()='Manage Orders']",
        "//a[@class='pc-link' and normalize-space()='Add New Order']",
        "//a[@class='pc-link' and normalize-space()='Paid Orders']",
        "//a[@class='pc-link' and normalize-space()='Unpaid Orders']",
        "//a[@class='pc-link' and normalize-space()='Packed Orders']",
        "//a[@class='pc-link' and normalize-space()='Delivered Orders']",
        "//a[@class='pc-link' and normalize-space()='Cancelled Orders']",
        "//a[@class='pc-link' and normalize-space()='Quote Orders']",
        "//a[@class='pc-link' and normalize-space()='Add Order Quote']"
    ]


    # your_apps_xpath = "//span[@class='pc-mtext' and normalize-space()='{name}']"

    # def get_app_item(self, name: str):
    #     return self.page.locator(self.your_apps_xpath.format(name=name))

    def scroll_to_the_end(self, locator: str):
        """Kiểm tra scroll đến vị trí cuối"""
        self.page.locator(locator).scroll_into_view_if_needed()

    def click_Your_app_menu(self):
        for index, item in enumerate(self.your_apps_items, start=1):
            self._click(item)
            self._take_screenshot(f"Your_app menu_{index}")

    def click_sub_Requests_menu(self):
        for index, item in enumerate(self.requests, start=1):
            self._click(self.your_apps_items[5])
            self.scroll_to_the_end(self.your_apps_items[5])
            self._click(item)
            self._take_screenshot(f"Your_app menu_{index}")
    def click_sub_coreHR_menu(self):
        for index, item in enumerate(self.c, start=1):
            self._click(self.your_company_items[2])
            self.scroll_to_the_end(self.your_company_items[2])
            self._click(item)
            self._take_screenshot(f"Your_app menu_{index}")

    def click_all_your_company_menu(self):
        self.scroll_to_the_end(self.your_company_items[0])
        for index, item in enumerate(self.your_company_items, start=1):
            self._click(item)
            self._take_screenshot(f"Your_company{index}") 
            if index + 1 < len(self.your_company_items):
                self.scroll_to_the_end(self.your_company_items[index])
                

    def click_all_Your_app_menu(self):
        self.click_Your_app_menu()
        self.click_sub_Requests_menu()
        self.click_all_your_company_menu()

