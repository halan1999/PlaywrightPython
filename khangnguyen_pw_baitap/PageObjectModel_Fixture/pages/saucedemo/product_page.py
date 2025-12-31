from playwright.sync_api import Page, expect
from pages.base_page import BasePage


class ProductPage(BasePage):
    # Locators
    _products_title = '//span[text()="Products"]'
    _shopping_cart_icon = '//a[@data-test="shopping-cart-link"]'

    def __init__(self, page: Page):
        super().__init__(page)

    def is_product_page_loaded(self, timeout: int = 5000) -> bool:
        try:
            expect(self.page.locator(self._products_title)).to_be_visible(timeout=timeout)
            expect(self.page.locator(self._shopping_cart_icon)).to_be_visible(timeout=timeout)
            return True
        except AssertionError:
            return False
