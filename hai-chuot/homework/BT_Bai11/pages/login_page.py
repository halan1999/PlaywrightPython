from playwright.sync_api import Page, expect
from core.base_page import BasePage

class LoginPage(BasePage):
    def __init__(self, page : Page, base_url : str):
        super().__init__(page)
        self.page = page
        self.base_url = base_url
        self.FORM_LOGIN = self.page.locator('//div[contains(@class,"minimal__layout__main__content")]')
        self.IPT_EMAIL = self.page.get_by_role("textbox", name = "Email address", exact = True)
        self.IPT_PASSWORD = self.page.get_by_role("textbox", name = "Password", exact = True)
        self.BTN_LOGIN = self.page.get_by_role("button", name = "Login account", exact = True)
        self.TXT_SUCCESS_MESSAGE = self.page.get_by_role("region", name = "Notifications alt+T")

    def login(self, email : str, password : str):
        self._navigate_url(self.base_url)
        self._verify_element_visible(self.FORM_LOGIN)

        self._set_text(self.IPT_EMAIL, email)
        self._set_text(self.IPT_PASSWORD, password)
        self._click(self.BTN_LOGIN)

    def verify_login_successful(self):
        expect(self.TXT_SUCCESS_MESSAGE).to_have_text('Login successfully.')