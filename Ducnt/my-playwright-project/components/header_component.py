from cores.base_page import BasePage

class header_component(BasePage):
    LOGO = "//a[@href='https://hrm.anhtester.com/erp/desk' and @class = 'b-brand']"
    Acount_setting = "//li//a[@data-original-title='Account Settings']"
    Apps = "//span[normalize-space(.)='Apps']"
    Apps_Events = "//a[@href='https://hrm.anhtester.com/erp/events-list']"
    Apps_Hollidays = "//a[@href='https://hrm.anhtester.com/erp/holidays-list']"
    Apps_Visitor_Book = "//a[@href='https://hrm.anhtester.com/erp/visitors-list']"
    Apps_Conference_Booking = "//a[@href='https://hrm.anhtester.com/erp/meeting-list']"
    Apps_Documents_Manager = "//a[@href='https://hrm.anhtester.com/erp/upload-files']"
    Apps_Assests = "//a[@href='https://hrm.anhtester.com/erp/assets-list' and @class='dropdown-item']"
    Apps_Awards = "//a[@href='https://hrm.anhtester.com/erp/awards-list']"
    Apps_Transfer = "//a[@href='https://hrm.anhtester.com/erp/transfers-list']"
    Apps_Complaints = "//a[@href='https://hrm.anhtester.com/erp/complaints-list']"
    Apps_Resignation = "//a[@href='https://hrm.anhtester.com/erp/resignation-list']"
    Apps_Customs_Fields = "//a[@href='https://hrm.anhtester.com/erp/custom-fields']"
    System_Calendar = "//a[@href='https://hrm.anhtester.com/erp/system-calendar']"
    System_Report = "//a[@href = 'https://hrm.anhtester.com/erp/system-reports']"
    To_Do_list = "//a[@href = 'https://hrm.anhtester.com/erp/todo-list']"
    ACCOUNT = "//span[@class='user-name']/ancestor::a"
    My_Account = "//span[normalize-space(.)='My Account']"
    Logout = "//a[@href='https://hrm.anhtester.com/erp/system-logout']"

    Click_element_header = {
        "Logo": LOGO,
        "Acount_setting": Acount_setting,
        "Apps": Apps,
        "Apps_Events": Apps_Events,
        "Apps_Hollidays": Apps_Hollidays,
        "Apps_Visitor_Book": Apps_Visitor_Book,
        "Apps_Conference_Booking": Apps_Conference_Booking,
        "Apps_Documents_Manager": Apps_Documents_Manager,
        "Apps_Assests": Apps_Assests,
        "Apps_Awards": Apps_Awards,
        "Apps_Transfer": Apps_Transfer,
        "Apps_Complaints": Apps_Complaints,
        "Apps_Resignation": Apps_Resignation,
        "Apps_Customs_Fields": Apps_Customs_Fields,
        "System_Calendar": System_Calendar,
        "System_Report": System_Report,
        "To_Do_list": To_Do_list,
        "ACCOUNT": ACCOUNT,
        "My_Account": My_Account
    }

    def click_and_screenshot_header(self):
        for name, locator in self.Click_element_header.items():
            try:
                self._click(locator, name)
                self._take_screenshot(f"Header_{name}.png")
                self.page.wait_for_load_state("networkidle")
            except Exception as e:
                print(f"[Lỗi] Không thể click vào {name}: {e}")


