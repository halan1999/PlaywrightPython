from playwright.sync_api import Page, expect

class CartPage:
    cart_item = "[class = 'cart_item']"
   
    def __init__(self, page: Page):
        self.page = page

    def verify_item_in_cart(self, item_name: str):
        expect(self.page.locator(self.cart_item)).to_contain_text(item_name)
        print(f"✅ Add product [{item_name}] to cart successfuly.")