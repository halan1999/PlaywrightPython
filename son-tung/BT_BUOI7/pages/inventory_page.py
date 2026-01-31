from BT_BUOI7.pages.base_page import BasePage

class InventoryPage(BasePage):
    CART_ICON = ".shopping_cart_link"
    SHOPPING_CART_BADGE = ".shopping_cart_badge"

    def add_item_to_cart(self, lstProducts : list):
        for product in lstProducts:
            self._click(f"//button[@id='add-to-cart-sauce-labs-{product}']", "Add products")

    def assert_cart_badge_count(self, expected_count: str):
        badge_text = self._get_locator(self.SHOPPING_CART_BADGE).inner_text()
        assert badge_text == expected_count, f"Expected {expected_count}, got {badge_text}"
        return True
