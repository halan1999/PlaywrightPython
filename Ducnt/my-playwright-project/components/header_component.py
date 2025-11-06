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

    def click_logo(self):
        self._click(self.LOGO, "Logo")
    
    def click_account_setting(self):
        self._click(self.Acount_setting, "Account setting")
    
    def click_apps(self):
        self._click(self.Apps, "Apps")
        self.page.wait_for_load_state("networkidle")
    
    def click_apps_events(self):
        self._click(self.Apps_Events, "Apps Events")

    def click_apps_hollidays(self):
        self._click(self.Apps_Hollidays, "Apps Hollidays")
    
    def click_apps_visitor_book(self):
        self._click(self.Apps_Visitor_Book, "Apps Visitor Book")

    def click_apps_conference_booking(self):
        self._click(self.Apps_Conference_Booking, "Apps Conference Booking")

    def click_apps_documents_manager(self):
        self._click(self.Apps_Documents_Manager, "Apps Documents Manager")

    def click_apps_assests(self):
        self._click(self.Apps_Assests, "Apps Assests")

    def click_apps_awards(self):
        self._click(self.Apps_Awards, "Apps Awards")

    def click_apps_transfer(self):
        self._click(self.Apps_Transfer, "Apps Transfer")

    def click_apps_complaints(self):
        self._click(self.Apps_Complaints, "Apps Complaints")

    def click_apps_resignation(self):
        self._click(self.Apps_Resignation, "Apps Resignation")

    def click_apps_customs_fields(self):
        self._click(self.Apps_Customs_Fields, "Apps Customs Fields")

    def click_system_calendar(self):
        self._click(self.System_Calendar, "System Calendar")

    def click_system_report(self):
        self._click(self.System_Report, "System Report")

    def click_to_do_list(self):
        self._click(self.To_Do_list, "To Do list")

    def click_account(self):
        self._click(self.ACCOUNT, "Account")
        self.page.wait_for_load_state("networkidle")   
