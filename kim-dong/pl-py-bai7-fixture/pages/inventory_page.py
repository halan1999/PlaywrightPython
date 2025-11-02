import random
from pages.base_page import BasePage

class InventoryPage(BasePage):
    """Đại diện cho trang danh sách sản phẩm (Inventory Page)."""

    PRODUCT_NAME_LOCATOR = ".inventory_item_name"
    ADD_TO_CART_BUTTONS = ".inventory_item button"
    CART_ICON = ".shopping_cart_link"
    CART_ITEM_NAMES = ".cart_item .inventory_item_name"

    def __init__(self, page: Page):
        self.page = page

    def get_all_product_names(self):
        return self.page.locator(self.PRODUCT_NAME_LOCATOR).all_inner_texts()

    def add_random_product_to_cart(self):
        product_names = self.get_all_product_names()
        selected_product = random.choice(product_names)
        print(f"[INFO] Selected product: {selected_product}")

        # Find the index of the selected product
        all_names = self.page.locator(self.PRODUCT_NAME_LOCATOR)
        count = all_names.count()
        for i in range(count):
            name = all_names.nth(i).inner_text()
            if name == selected_product:
                self.page.locator(self.ADD_TO_CART_BUTTONS).nth(i).click()
                break

        return selected_product

    def go_to_cart(self):
        self.page.locator(self.CART_ICON).click()

    def assert_product_in_cart(self, expected_name):
        cart_items = self.page.locator(self.CART_ITEM_NAMES).all_inner_texts()
        print(f"[DEBUG] Cart contains: {cart_items}")
        assert expected_name in cart_items, f"Expected '{expected_name}' in cart, but got {cart_items}"