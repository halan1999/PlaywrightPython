from playwright.sync_api import expect
from pages.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, page, login_url):
        super().__init__(page)
        self.login_url = login_url
        self.username_input = '//input[@name="username"]'
        self.password_input = '//input[@name="password"]'
        self.login_button = '//button[normalize-space()="Login"]'

        self._twitter_icon = '//a[contains(@href,"twitter")]'

    def open(self):
        self.page.goto(self.login_url)
        expect(self.page.locator(self.username_input)).to_be_visible()

    def click_twitter_icon(self):
        self.expect_visible(self._twitter_icon)
        self.click(self._twitter_icon)


    def login(self, username, password):
        self.fill(self.username_input, username)
        self.fill(self.password_input, password)
        self.click(self.login_button)
