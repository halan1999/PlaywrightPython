from playwright.sync_api import expect
from pages.base_page import BasePage
from pages.x_page import XPage


class LoginPage(BasePage):
    _username_input = '//input[@name="username"]'
    _password_input = '//input[@name="password"]'
    _login_button = '//button[normalize-space()="Login"]'
    _twitter_icon = '//a[contains(@href,"twitter")]'

    def __init__(self, page, login_url):
        super().__init__(page)
        self.login_url = login_url

    def open(self):
        self.page.goto(self.login_url)
        expect(self.page.locator(self._username_input)).to_be_visible()

    def click_twitter_icon(self):
        self.expect_visible(self._twitter_icon)
        self.click(self._twitter_icon)

    def open_x_page(self):
        with self.page.context.expect_page() as new_page_info:
            self.click_twitter_icon()
        x_tab = new_page_info.value
        return XPage(x_tab)

    def login(self, username, password):
        self.fill(self._username_input, username)
        self.fill(self._password_input, password)
        self.click(self._login_button)
