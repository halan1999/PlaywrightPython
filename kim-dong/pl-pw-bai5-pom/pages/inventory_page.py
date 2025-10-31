from pages.base_page import BasePage

class InventoryPage(BasePage):
    """Đại diện cho trang danh sách sản phẩm (Inventory Page)."""

    ITEM_BACKPACK_ADD_BUTTON = "[data-test='add-to-cart-sauce-labs-backpack']"
    SHOPPING_CART_BADGE = ".shopping_cart_badge"
    SHOPPING_CART_ICON = ".shopping_cart_link"
    ITEM_IN_CART =".inventory_item_name"

    def add_backpack_to_cart(self):
        """Thêm sản phẩm 'Sauce Labs Backpack' vào giỏ hàng."""
        self._click(self.ITEM_BACKPACK_ADD_BUTTON, "Add Backpack")

    def assert_cart_badge_count(self, expected_count: str):
        """Kiểm tra số lượng sản phẩm trong giỏ hàng."""
        badge_text = self._get_locator(self.SHOPPING_CART_BADGE).inner_text()
        print(f"[DEBUG] Expected: {expected_count}, Actual: {badge_text}")
        assert badge_text == expected_count, f"Expected {expected_count}, got {badge_text}"


    def add_product_to_cart(self):
        self._click(self.ITEM_BACKPACK_ADD_BUTTON, "Add Backpack")        

    def assert_product_in_cart(self,expected_product_name:str):
        self._click(self.SHOPPING_CART_ICON,"Open Cart")
        actual_product_name = self._get_locator(self.ITEM_IN_CART).inner_text()
        print(f"[DEBUG] Expected: {expected_product_name}, Actual: {actual_product_name}")
        assert actual_product_name == expected_product_name, f"Expected {expected_product_name}, got {actual_product_name}"
        

