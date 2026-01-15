from playwright.sync_api import Page, expect
from pages.base_page import BasePage
import json
from pathlib import Path


class LoginPage(BasePage):
    url = "https://book.anhtester.com/sign-in"

    # Locators
    _email_field = '//input[@name="email"]'
    _password_field = '//input[@name="password"]'
    _login_button = '//button[normalize-space()="Login account"]'
    _login_success_message = '//p[text()="Login successfully."]'

    _cred_path = (
        Path(__file__).resolve().parents[2]
        / "resources"
        / "books"
        / "login_credentials.json"
    )

    with open(_cred_path, "r", encoding="utf-8") as f:
        _creds = json.load(f)

    login_creds = _creds[-1]
    username_valid = login_creds["email_address"]
    password_valid = login_creds["password"]

    def __init__(self, page: Page):
        super().__init__(page)
        self._username = page.locator(self._email_field)
        self._password = page.locator(self._password_field)
        self._login_btn = page.locator(self._login_button)
        self._toast_invalid = page.locator('//div[text()="Invalid Login Credentials."]')
        self._my_profile = page.locator('//a[contains(@href,"my-profile")]//p')

    def open(self):
        self.page.goto(self.url, wait_until="domcontentloaded", timeout=60000)

    def is_login_page_loaded(self):
        expect(self._username).to_be_visible(timeout=5000)
        expect(self._password).to_be_visible(timeout=5000)

    def login_valid(self, username: str | None = None, password: str | None = None):
        self._username.fill(username or self.username_valid)
        self._password.fill(password or self.password_valid)
        self._login_btn.click()
    
    def is_logged_in(self, timeout: int = 8000) -> bool:
        try:
            expect(self._login_success_message).to_be_visible(timeout=timeout)
            return True
        except AssertionError:
            return False