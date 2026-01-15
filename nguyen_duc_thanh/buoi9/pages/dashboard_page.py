import time
from buoi9.pages.base_page import BasePage


class DashBoardPage(BasePage):
    def __init__(self, page):
        super().__init__(page)

    DASHBOARD_MENU = "//span[@class='oxd-text oxd-text--span oxd-main-menu-item--name'][normalize-space()='Dashboard']"
    PROFILE_DROPDOWN = "//i[@class='oxd-icon bi-caret-down-fill oxd-userdropdown-icon']"
    LOGOUT_BTN = "//a[normalize-space()='Logout']"
    H5 = "//h5[@class='oxd-text oxd-text--h5 orangehrm-login-title']"

    def get_heading5(self):
        return self.get_text(self.H5)
    
    def assert_dashboard_screen(self):
        return self.get_locator(self.DASHBOARD_MENU).is_visible()
    
    def assert_loggout_successfully(self):
        self.click_element(self.PROFILE_DROPDOWN)
        self.click_element(self.LOGOUT_BTN)
        time.sleep(3)
        return self.get_locator(self.H5).is_visible()