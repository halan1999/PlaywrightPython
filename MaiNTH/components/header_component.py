from core.base_page import BasePage

class HeaderComponent (BasePage):
    LOGO = "//a[@class='b-brand']//img[@class='logo logo-lg']"
    ACCOUNT_SETTING = "//a[@data-original-title='Account Settings']"
    APP = "//span[@data-toggle='tooltip']"
    CALENDAR = "//a[@href='https://hrm.anhtester.com/erp/system-calendar']"
    SYSTEM_REPORT = "//a[@href='https://hrm.anhtester.com/erp/system-reports']"
    LANGUAGE = "(//a[@role='button'])[2]"
    TODOLIST = "//a[@class='pc-head-link mr-0']//*[name()='svg']"

    USER = "(//a[@role='button'])[3]"
    MY_ACCOUNT = "//span[normalize-space()='My Account']"
    LOG_OUT = "//span[normalize-space()='Logout']"



    def open_account_setting (self):
        self._click (self.ACCOUNT_SETTING, "account setting menu")
        self._take_screenshot("open_account_setting")

    def open_apps(self):
        self._click (self.APP, "app menu")
        self._take_screenshot("open_apps")

    def open_calendar(self):
        self._click (self.CALENDAR, "calendar menu")
        self._take_screenshot("open_calendar")

    def open_system_report(self):
        self._click(self.SYSTEM_REPORT, "system report menu")
        self._take_screenshot("open_system_report")

    def open_language(self):
        self._click(self.LANGUAGE, "language")
        self._take_screenshot("open_language")

    def open_todolist(self):
        self._click(self.TODOLIST, "todo list")
        self._take_screenshot("open_todolist")

    def click_user(self):
        self._click(self.USER, "user")
        self._take_screenshot("click_user")

    def click_my_account(self):
        self._click(self.MY_ACCOUNT,"my account")

    def click_logout(self):
        self._click(self.LOG_OUT, "log out")
        self._take_screenshot("click_logout")

    

