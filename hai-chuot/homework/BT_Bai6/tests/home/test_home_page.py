import pytest
from components.header_component import XpathHeader

@pytest.mark.usefixtures("login_pass_page")
class TestHomePage:
    def test_click_header(self):
        lst_xpath_header_enum = [
            XpathHeader.ACCOUNT_SETTING,
            XpathHeader.SYSTEM_CALENDAR,
            XpathHeader.SYSTEM_REPORT,
            XpathHeader.TODO_LIST
        ]

        for i, xpath_header_enum in enumerate(lst_xpath_header_enum, start=1):
            self.home_page.click_header_function(xpath_header_enum)
            self.home_page._take_screenshot(f'header/header_function_{i}.png')

    def test_click_apps_icon(self):
        lst_apps_items = [
            "Events",
            "Holidays",
            "Visitor Book",
            "Conference Booking",
            "Documents Manager",
            "Assets",
            "Awards",
            "Transfers",
            "Complaints",
            "Resignations",
            "Custom Fields"
        ]

        for i, apps_items in enumerate(lst_apps_items, start=1):
            self.home_page.click_apps_header_function(XpathHeader.APPS, apps_items)
            self.home_page._take_screenshot(f'apps_menu/apps_subfunction_{i}.png')

    def test_click_single_header(self):
        lst_menu_items = [
            "Home",
            "Attendance",
            "Projects",
            "Tasks",
            "Payroll",
            "Helpdesk",
            "Training Sessions",
            "Employees",
            "Recruitment (ATS)",
            "Finance",
            "Manage Clients",
            "Leads",
            "Invoices",
            "Estimates",
            "Disciplinary Cases"
        ]

        for i, menu_item in enumerate(lst_menu_items, start=1):
            self.home_page.click_menu_function(menu_item)
            self.home_page._take_screenshot(f'single_menu/menu_{i}.png')

    def test_click_corehr_menu(self):
        lst_menu_hr = [
            "Department",
            "Designation",
            "Policies",
            "Make Announcement",
            "Organization Chart"
        ]

        for i, menu_hr in enumerate(lst_menu_hr, start=1):
            self.home_page.click_sub_menu_function("Core HR" , menu_hr)
            self.home_page._take_screenshot(f'corehr_menu/menu_{i}.png')