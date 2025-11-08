from ..core.base_page import BasePage
from playwright.sync_api import expect
import time


class InventoryPage(BasePage):
    URL = "https://www.saucedemo.com/inventory.html"
    INVENTORY_ITEM = '.inventory_item'
    CART_BADGE = '.shopping_cart_badge'

    def visit_inventory_page(self):
        self._visit(self.URL)

    def add_item_to_cart_by_name(self, item_name: str):
        item_locator = f"{self.INVENTORY_ITEM}:has-text('{item_name}')"
        add_button_locator = f"{item_locator} button:has-text('Add to cart')"
        self._click(add_button_locator, f"Add to cart button for '{item_name}'")

    def get_cart_count(self):
        
        return self._get_locator(self.CART_BADGE)