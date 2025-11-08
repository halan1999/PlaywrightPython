from core.base_page import BasePage, expect
import time

class CartPage(BasePage):
    Title_cart_locator = "[data-test='title']"
    Cart_list = "//div[@class='cart_list']"
    Cart_item = '[data-test="inventory-item"]'
    BTN_Conti_Shop = "#continue-shopping"
    BTN_Checkout = "[data-test='checkout']"

    Title = "Your Cart"

    def Verify_title(self):
        self._verify_text(self.Title_cart_locator,self.Title)
        print(f"Title is {self.Title}")

    def Verify_2items_in_cart(self):
        self._verify_count(self.Cart_item,2)
        print(f"There are 2 items in your cart!")


