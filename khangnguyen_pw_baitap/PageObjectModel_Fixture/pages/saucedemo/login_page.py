from playwright.sync_api import Page, expect
from pages.base_page import BasePage


class LoginPage(BasePage):
    # Locators
    USERNAME_INPUT = '//input[@id="user-name"]'
    PASSWORD_INPUT = '//input[@id="password"]'
    LOGIN_BUTTON = '//input[@id="login-button"]'
    LOCKED_OUT_ERROR = '//h3[normalize-space()="Epic sadface: Sorry, this user has been locked out."]'

    URL = "https://www.saucedemo.com/"

    def __init__(self, page: Page):
        super().__init__(page)

    def open(self):
        self.page.goto(self.URL)

    def login(self, username: str, password: str):
        self.page.fill(self.USERNAME_INPUT, username)
        self.page.fill(self.PASSWORD_INPUT, password)
        self.page.click(self.LOGIN_BUTTON)

    def is_login_failed(self) -> bool:
        return self.page.locator(self.LOCKED_OUT_ERROR).is_visible()
