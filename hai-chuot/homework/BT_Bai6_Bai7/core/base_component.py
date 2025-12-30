
from playwright.sync_api import Page, expect

class BaseComponent:
    def __init__(self, page : Page):
        self.page = page

    def _click_two_component(self, xpath_element1 : str, xpath_element2 : str):
        """
        Thực hiện click vào các component dạng dropdown list
        """
        locator_element1 = self.page.locator(xpath_element1)
        locator_element2 = self.page.locator(xpath_element2)
        
        locator_element1.click()
        expect(locator_element2).to_be_visible()
        locator_element2.click()