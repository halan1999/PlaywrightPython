from core.base_page import BasePage
import time

class HeaderComponent(BasePage):
    """Đại diện cho thanh header hiển thị trên mọi trang."""

    # logo = "//div[@class='pcm-logo']"
   
    # account_setting = "[data-original-title='Account Settings']"
    # apps = "//a[@class='pc-head-link active dropdown-toggle arrow-none mr-0']"
    # system_calendar = "[data-original-title='System Calendar']"
    # system_report = "[data-original-title='System Reports']"
    # language_locator = "//a[classs='pc-head-link dropdown-toggle arrow-none mr-0']"
    # language_locator = "//a[classs='pc-head-link dropdown-toggle arrow-none mr-0']"
    # to_do_list = "[data-original-title='Todo List']"
    btn_logout = "//a[@class='btn btn-smb btn-outline-primary rounded-pill']"
    profile_icon = "//header//a/*[@class='user-avatar']"
    logout_profile = "//span[normalize-space()='Logout']"

    header_items = [
        "//header//a[@data-original-title='Account Settings']",
        "//header//span[@data-original-title='Apps']",
        "//header//a[@data-original-title='System Calendar']",
        "//header//a[@data-original-title='System Reports']",
        "//header//li[1]//a[@data-toggle='dropdown']",
        "//header//a[@data-original-title='Todo List']"
    ]

    # def navigate_Acc_Setting(self):
    #     """Mở điều hướng đến trang Account Setting."""
    #     self._click(self.account_setting)
    #     self._take_screenshot("Account_Setting")

    # def navigate_System_Calendar(self):
    #     """Mở điều hướng đến trang System Calendar"""
    #     self._click(self.system_calendar)
    #     self._take_screenshot("System_Calendar")

    # def navigate_System_Reports(self):
    #     self._click(self.system_report)
    #     self._take_screenshot("System_Reports")

    # def choose_Language(self):
    #     self._click(self.language_locator)
    #     time(5)
    #     self._take_screenshot("Choose_Language")

    # def choose_Apps(self):
    #     self._click(self.apps)
    #     time(5)
    #     self._take_screenshot("Choose_Apps")

    # def navigate_ToDoList(self):
    #     self._click(self.to_do_list)
    #     self._take_screenshot("To_Do_List")

    def click_all_header_items(self):
        """Click on each header items"""
        for index, item in enumerate(self.header_items, start=1):
            self._click(item)
            self._take_screenshot(f"header_item_{index}")    

    def logout_by_button(self):
        """Đăng xuất khỏi hệ thống."""
        self._click(self.btn_logout)
        self._take_screenshot("Logout_by_button")

    def logout_on_profile(self):
        """Đăng xuất khỏi hệ thống."""
        self._click(self.profile_icon)
        self._click(self.logout_profile)
        self._take_screenshot("Logout_on_profile")


