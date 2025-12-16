from locators.home.home_locators import HomeLocators as HL
from core.base_page import BasePage

class HomePage(BasePage):
    def __init__(self, page):
        super().__init__(page)

    def _verify_home_page(self):
        self._expect_to_be_visible(HL.WELCOM_LABLE)

    def _logout(self):
        self._click(HL.LOGOUT_BUTTON)
        self._expect_to_have_url("/login")
        