from core.base_page import BasePage
from playwright.sync_api import Page, expect
from pages.new_window_page import NewWindowPage
from pages.twitter_page import Orange_TwitterPage
from pages.hrm_dashboard_page import HRM_DashboardPage
import json
class OrangeHrmPage(BasePage):

    URL = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    USERNAME_INPUT = "//input[@name='username']"
    PASSWORD_INPUT = "//input[@name='password']"
    LOGIN_BUTTON = "//button[@type='submit']"
    SOCIAL_ICONS = {
    "LINKEDIN_ICON": "//a[contains(@href,'orangehrm/mycompany/')]",
    "FACEBOOK_ICON": "//a[contains(@href,'facebook')]",
    "TWITTER_ICON": "//a[contains(@href,'twitter')]",
    "YOUTUBE_ICON": "//a[contains(@href,'youtube')]",
    }
    def __init__(self, page:Page):
        super().__init__(page)  

    def goto(self):
        self._goto(self.URL)
        self._take_screenshot("hrm_login_page")
        
    def load_credentials(self,type:str):
        with open(file = r'./BT_Buoi9/data/credentials.json', mode="r",encoding="utf-8") as file:
            credentials = json.load(file)
            return credentials[type]

    def login_with_valid_credentials(self):
        credentials = self.load_credentials("hrm_orange_user")
        self._fill(self.USERNAME_INPUT, credentials["username"])
        self._fill(self.PASSWORD_INPUT, credentials["password"])
        self._click(self.LOGIN_BUTTON)
        
        self.page.wait_for_url("**/dashboard/index", timeout=10000)
        self.page.wait_for_load_state("load")
        self._take_screenshot("after_login")
        return HRM_DashboardPage(self.page)

    def open_social_tab(self, icon_name: str):
        with self.page.context.expect_page() as new_page_info:
            self._click(self.SOCIAL_ICONS[icon_name]) 
        new_page = new_page_info.value
        new_page.wait_for_load_state()
        if icon_name == "TWITTER_ICON":
            return Orange_TwitterPage(new_page)     
        