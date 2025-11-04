from pages.base_page import BasePage
from playwright.sync_api import expect

class Inventory_page(BasePage):

    URL = "https://www.saucedemo.com/inventory.html"
    Inventory_item_name = "//div[normalize-space(.)='Sauce Labs Backpack']"
    Inventory_button_add_to_cart = "//button[@id='add-to-cart-sauce-labs-backpack']"
    Inventory_shopping_cart_badge = "//span[@class='shopping_cart_badge']"
   
    def goto(self):
     self._visit(self.URL)

    def add_to_cart(self):
        self._click(self.Inventory_button_add_to_cart, "Add to cart button")

    def assert_item_in_inventory(self):
        self._assert_text_visible(self.Inventory_item_name, "Sauce Labs Backpack")
    
    def assert_shopping_cart_badge(self):
        self._wait_for_element(self.Inventory_shopping_cart_badge)
        self._assert_text_visible(self.Inventory_shopping_cart_badge, "1")


