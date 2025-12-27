from playwright.sync_api import Page, expect
from pages.base_page import BasePage
import json
from pathlib import Path


class LoginPage(BasePage):
    url = "https://hrm.anhtester.com/erp/login"

    # Locators
    _username_field = '//input[@id="iusername" and @name="iusername"]'
    _password_field = '//input[@id="ipassword" and @name="password"]'
    _login_button = '//button[@type="submit"]'

    _cred_path = (
        Path(__file__).resolve().parents[2]
        / "resources"
        / "hrm_anhtester"
        / "login_credentials.json"
    )

    with open(_cred_path, "r", encoding="utf-8") as f:
        _creds = json.load(f)

    username_valid = _creds["valid"]["username"]
    password_valid = _creds["valid"]["password"]
    username_invalid = _creds["invalid"]["username"]
    password_invalid = _creds["invalid"]["password"]

    def __init__(self, page: Page):
        super().__init__(page)
        self._username = page.locator(self._username_field)
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

    def login_invalid(self, username: str | None = None, password: str | None = None):
        self._username.fill(username or self.username_invalid)
        self._password.fill(password or self.password_invalid)
        self._login_btn.click()

    def is_invalid_toast_visible(self, timeout: int = 5000) -> bool:
        try:
            expect(self._toast_invalid).to_be_visible(timeout=timeout)
            return True
        except AssertionError:
            return False

    def is_logged_in(self, timeout: int = 8000) -> bool:
        try:
            expect(self._my_profile).to_be_visible(timeout=timeout)
            return True
        except AssertionError:
            return False
