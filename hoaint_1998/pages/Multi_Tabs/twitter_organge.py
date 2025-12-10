from core.base_page import BasePage
from core.common_locators import CommonLocators as CL
from playwright.sync_api import Page

class TwitterOrange(BasePage):
    X_ICON = "//h1[@role='heading']/a[@aria-label='X']"
    NAME_PAGE = "//div[@data-testid='UserName']//span[normalize-space()='OrangeHRM']/parent::span"

    def __init__(self, page):
        super().__init__(page)
        self.page = page

    def _verify_twitter_orange_page(self):
        self._wait_for_element(self.X_ICON)
        self._wait_for_element(self.NAME_PAGE)