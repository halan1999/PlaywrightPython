from pages.base_page import BasePage
from pages.login_page import LoginPage
from playwright.sync_api import Page, expect

class  InventoryPage(BasePage):
    btn_cart = "//a[@class='shopping_cart_link']"
    table_cart_list = "//div[@class='cart_list']//div[@class='cart_item']"
    btn_continue = "//button[normalize-space()='Continue Shopping']"
    btn_checkout = "//button[normalize-space()='Checkout']"

    def goto_cart(self):
        self._click(self.btn_cart)
    
    def count_item(self):
        return self.page.locator(self.table_cart_list).count()

        

    

    
