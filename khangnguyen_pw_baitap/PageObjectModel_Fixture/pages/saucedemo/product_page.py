from playwright.sync_api import Page, expect
from pages.base_page import BasePage


class ProductPage(BasePage):
    # Locators
    PRODUCTS_TITLE = '//span[text()="Products"]'
    SHOPPING_CART_ICON = '//a[@data-test="shopping-cart-link"]'

    def __init__(self, page: Page):
        super().__init__(page)

    def is_product_page_loaded(self, timeout: int = 5000) -> bool:
        try:
            expect(self.page.locator(self.PRODUCTS_TITLE)).to_be_visible(timeout=timeout)
            expect(self.page.locator(self.SHOPPING_CART_ICON)).to_be_visible(timeout=timeout)
            return True
        except AssertionError:
            return False
