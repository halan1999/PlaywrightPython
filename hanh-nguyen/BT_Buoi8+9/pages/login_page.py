from playwright.sync_api import Page, expect
from core.base_page import BasePage

class LoginPage(BasePage):
    URL = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    INPUT_USERNAME = "//input[@placeholder='Username']"
    INPUT_PASSWORD = "//input[@placeholder='Password']"
    LOGIN_BUTTON = "//button[normalize-space()='Login']"
    LINKEDIN_ICON = "//a[contains(@href,'linkedin')]"
    FACEBOOK_ICON = "//a[contains(@href,'facebook')]"
    TWITTER_ICON = "//a[contains(@href,'twitter')]"
    YOUTUBE_ICON = "//a[contains(@href,'youtube')]"

    def __init__(self, page):
        super().__init__(page)

    def goto(self):
        self._goto(self.URL)

    def login(self, username: str, password: str):
        self._fill(self.INPUT_USERNAME, username)
        self._fill(self.INPUT_PASSWORD, password)
        self._click(self.LOGIN_BUTTON)

    def assert_login_successful(self):
        expect(self.page).to_have_url("https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index")

    def open_social_tab(self, icon_locator) -> Page:
        with self.page.context.expect_page() as new_pages:
            self.page.locator(icon_locator).click()

        new_tab = new_pages.value
        new_tab.wait_for_load_state()
        return new_tab
