import json

from BT_BUOI12.core.base_page import BasePage
from BT_BUOI12.pages.multitabs.new_social_page import NewPage
from playwright.sync_api import Page
from playwright.sync_api import expect

class OrangePage(BasePage):
    URL = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    heading = "h5"
    click_linkedin = "//div[@class='orangehrm-login-footer-sm']//a[1]"
    click_facebook = "//div[@class='orangehrm-login-footer-sm']//a[2]"
    click_twitter = "//div[@class='orangehrm-login-footer-sm']//a[3]"
    click_youtube = "//div[@class='orangehrm-login-footer-sm']//a[4]"

    USERNAME_FIELD = "//input[@name='username']"
    PASSWORD_FIELD = "//input[@name='password']"
    LOGIN_BUTTON = "//button[@type='submit']"
    LOGOUT_BUTTON = "//a[normalize-space()='Logout']"
    AVATAR = "//span//img"

    dashboard_label = "h6"

    def __init__(self, page):
        super().__init__(page)

    def open_url(self):
        self._visit(self.URL)

    def get_heading_text(self) -> str:
        return self._get_text(self.heading)

    def open_new_tab_and_return_page_object(self, button_page) -> NewPage:
        with self.page.context.expect_page() as new_page_info:
            self._click(button_page)

        new_page = new_page_info.value
        new_page.wait_for_load_state()

        # Trả về POM cho tab mới
        return NewPage(new_page)

    def login(self):
        self.open_url()

        with open("BT_BUOI12/data/users.json") as f:
            user = json.load(f)

        self._fill(self.USERNAME_FIELD, user["username"])
        self._fill(self.PASSWORD_FIELD, user["password"])
        self._click(self.LOGIN_BUTTON)

    def verify_element(self):
        self._assert_text_visible(self.dashboard_label, 'Dashboard')

    def logout(self):
        self._click(self.AVATAR)
        self._click(self.LOGOUT_BUTTON, "Logout button")
