from playwright.sync_api import Page

class InventoryPage:
    def __init__(self, page: Page):
        self.page = page
        self.inventory_item_add_button = "button[data-test='add-to-cart-sauce-labs-backpack']"
        self.cart_icon = "a.shopping_cart_link"

    def add_product_to_cart(self):
        """Nhấn nút Add to cart"""
        self.page.click(self.inventory_item_add_button)

    def go_to_cart(self):
        self.page.click(self.cart_icon)
