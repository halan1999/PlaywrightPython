
from buoi5.pages.base_page import BasePage


class InventoryPage(BasePage):
    ADD_TO_CART_BACKPACK_BTN = "//button[@id='add-to-cart-sauce-labs-backpack']"
    SHOPPING_CART_BADGE = "//span[@class='shopping_cart_badge'][@data-test='shopping-cart-badge']"

    def _add_to_cart_backpack(self):
        self._click(self.ADD_TO_CART_BACKPACK_BTN)

    def _verify_backpack_is_added(self, quantity):
        badge_count = self._get_locator(self.SHOPPING_CART_BADGE).inner_text()
        assert badge_count == quantity,f"Expected: {quantity}, got {badge_count}"


    