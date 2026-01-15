from buoi9.pages.base_page import BasePage

from buoi9.pages.dashboard_page import DashBoardPage
from buoi9.pages.multi_tab.twitter_page import TwitterPage



class LoginPage(BasePage):

    URL = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    TWITTER_ICON = "//a[@href='https://twitter.com/orangehrm?lang=en']"
    H5 = "//h5[@class='oxd-text oxd-text--h5 orangehrm-login-title']"
    USERNAME = "//input[@placeholder='Username']"
    PASSWORD = "//input[@placeholder='Password']"
    LOGIN_BTN = "//button[@type='submit']"
    def __init__(self, page):
        super().__init__(page)

    def get_heading5(self):
        return self.get_text(self.H5)

    def go_to_loginpage(self):
        self.goto(self.URL)

    def login(self,username,password):
        self.send_text(self.USERNAME,username)
        self.send_text(self.PASSWORD,password)
        self.click_element(self.LOGIN_BTN)
        return DashBoardPage(self.page)

    def logged(self):
        self.send_text(self.USERNAME,"Admin")
        self.send_text(self.PASSWORD,"admin123")
        self.click_element(self.LOGIN_BTN)
        return DashBoardPage(self.page)

    def open_twitter_tab(self) -> TwitterPage:
        with self.page.context.expect_page() as new_page_info:
            self.click_element(self.TWITTER_ICON)

        new_page = new_page_info.value
        new_page.wait_for_load_state()
        return TwitterPage(new_page)
