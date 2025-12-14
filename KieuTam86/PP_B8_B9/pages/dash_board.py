from core.base_page import BasePage, expect
import time

class Dashboard(BasePage):

    DASHBOARD_TITLE = "h6:has-text('Dashboard')"
    USER_MENU = "span.oxd-userdropdown-tab"
    LOGOUT = "a:has-text('Logout')"
    DASHBOARD_URL = "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"

    # def __init__(self, page):
    #     super.__init__(page)

    def verify_dashboard_displayted(self):
        self._verify_url_contains(self.DASHBOARD_URL)
        self._verify_text(self.DASHBOARD_TITLE,"Dashboard")
        print(f"Title :{self.DASHBOARD_TITLE}")

    def logout(self):
        self._click(self.USER_MENU)
        self._click(self.LOGOUT)    



