from core.base_page import BasePage

class DashboardPage(BasePage):

    DASHBOARD_HEADER = "//div[@class='oxd-topbar-header']"
    USER_MENU = "//span[@class='oxd-userdropdown-tab']"
    LOGOUT = "//a[text()='Logout']"

    def assert_dashboard_visible(self):
        self._assert_text_visible(self.DASHBOARD_HEADER)

    def logout(self):
        self._click(self.USER_MENU)
        self._click(self.LOGOUT)
