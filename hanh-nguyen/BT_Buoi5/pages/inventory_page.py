from .base_page import BasePage
from playwright.sync_api import Playwright, expect

class InventoryPage(BasePage):
    product_filter = "//select[@class='product_sort_container']"
    highest_price_filter = "//select[@class='product_sort_container']//option[@value='hilo']"
    add_button_highest_price = "(//div[@class='inventory_list']//button)[1]"
    remove_button = "//button[normalize-space()='Remove']"
    shopping_cart_badge = "//span[@class = 'shopping_cart_badge']"
        
    def filter_by_highest_price(self):
        self._click(self.product_filter)
        self._click(self.highest_price_filter)

    def add_to_cart(self):
        self._click(self.add_button_highest_price)

    def assert_cart_badge_count(self, expected_count: str):
        badge = self._get_locator(self.shopping_cart_badge)
        expect(badge).to_have_text(expected_count)

    def remove_product(self):
        self._click(self.remove_button)



