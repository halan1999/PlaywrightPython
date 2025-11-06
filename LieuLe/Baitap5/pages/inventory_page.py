from playwright.sync_api import Page, expect

class InventoryPage:
    product_container = "[data-test = 'inventory-item']"
    add_to_cart_btt = "//button[normalize-space(text()) = 'Add to cart']"
    cart_icon = "[data-test = 'shopping-cart-link']"

    def __init__(self, page: Page):
        self.page = page

    def add_product_to_cart(self, product_name: str):
        product = self.page.locator(self.product_container).filter(has_text=product_name)
        expect(product).to_have_count(1)
        product.locator(self.add_to_cart_btt).click()

    def go_to_cart(self):
        self.page.click(self.cart_icon)

    