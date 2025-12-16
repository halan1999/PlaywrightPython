from core.base_page import BasePage, expect
from pages.dash_board import Dashboard
# from pages.lindln_page import LindlnPage
from components.social_footer import Social_Footer
import time, json

class Oranage_HRM(BasePage):
    #Save locator & action of Oranage_HRM page

    URL = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    TITLE = "h5"
    USERNAME_LOCATOR = "//input[@name='username']"
    USERNAME_PLACEHOLDER = "//input[@placeholder='username']"
    PASSWORD_LOCATOR = "//input[@name='password']"
    PASSWORD_PLACEHOLDER = "//input[@placeholder='password']"
    BTN_LOGIN_LOCATOR = "//button[@type='submit']"
    LINDLN_LOCATOR = "//a[@target='_blank'][1]"
    LINDLE_URL = "https://www.linkedin.com/company/orangehrm/"
    FACEBOOK_LOCATOR = "//a[@target='_blank'][2]"
    TWISTER_LOCATOR = "//a[@target='_blank'][3]"
    YOUTUBE_LOCATOR = "//a[@target='_blank'][4]"

    def __init__(self, page):
        self.page = page

    def load_credentials(self):
        with open("data/credentials.json","r") as f:
            return json.load(f)

    def goto(self):
        self._open_page(self.URL)
        self._take_screenshot("Open_login_page")


    def  check_form_login(self):
        self.goto()
        self._verify_locator_visible(self.TITLE)
        self._verify_locator_visible(self.USERNAME_LOCATOR)
        self._verify_locator_visible(self.PASSWORD_LOCATOR)
        self._verify_locator_visible(self.BTN_LOGIN_LOCATOR)
        self._verify_text(self.TITLE,"Login")
        self._verify_locator_visible(self.LINDLN_LOCATOR)
        self._verify_locator_visible(self.FACEBOOK_LOCATOR)
        self._verify_locator_visible(self.TWISTER_LOCATOR)
        self._verify_locator_visible(self.YOUTUBE_LOCATOR)


    def login_valid_user(self):
        creds = self.load_credentials()
        # self.goto()
        self._fill(self.USERNAME_LOCATOR, creds["valid_user"]["username"])
        self._fill(self.PASSWORD_LOCATOR, creds["valid_user"]["password"])
        self._take_screenshot("Input_User_Password")
        self._click(self.BTN_LOGIN_LOCATOR)
        self._take_screenshot("Home")

    def click_icon_twister(self) -> Social_Footer:
        with self.page.context.expect_page() as new_page_info:
            self.page.click(self.TWISTER_LOCATOR)
        new_tab = new_page_info.value
        new_tab.wait_for_load_state()
        return new_tab
    
    def click_icon_facebook(self) -> Social_Footer:
        with self.page.context.expect_page() as new_page_info:
            self.page.click(self.FACEBOOK_LOCATOR)
        new_tab = new_page_info.value
        new_tab.wait_for_load_state()
        return new_tab
    
    def click_icon_youtube(self) -> Social_Footer:
        with self.page.context.expect_page() as new_page_info:
            self.page.click(self.YOUTUBE_LOCATOR)
        new_tab = new_page_info.value
        new_tab.wait_for_load_state()
        return new_tab
    
    def verify_dashboard(self):
        dashboard = Dashboard(self.page)
        dashboard.verify_dashboard_displayted()

    def logout(self):
        dashboard = Dashboard(self.page)
        dashboard.logout()

    def bring_to_front(self):
        self.page.bring_to_front()    
    


