from pages.base_page import BasePage

class InventoryPage(BasePage):
    inventory_logo = "//div[@class ='app_logo']"
    BTN_Product_1 = "#add-to-cart-sauce-labs-backpack"
    BTN_Product_2 = "#add-to-cart-sauce-labs-bike-light"
    BTN_Product_3 = "#add-to-cart-sauce-labs-bolt-t-shirt"
    BTN_Product_4 = "#add-to-cart-sauce-labs-fleece-jacket"
    BTN_Product_5 = "#add-to-cart-sauce-labs-onesie"
    BTN_Product_6 = "add-to-cart-test.allthethings()-t-shirt-(red)"
    Cart_locator = "//a[@class='shopping_cart_link']"
    Cart_count = "//span[@class='shopping_cart_badge']"
    
    def verify_login_success(self):
        self._verify_text(self.inventory_logo, "Swag Labs")

    def add_P1_to_cart(self):
        self._click(self.BTN_Product_1)
        print("Add product to Cart successfully!")

    def add_P2_to_cart(self):
        self._click(self.BTN_Product_2)
        print("Add product to Cart successfully!")

    def add_P3_to_cart(self):
        self._click(self.BTN_Product_3)
        print("Add product to Cart successfully!")

    def add_P4_to_cart(self):
        self._click(self.BTN_Product_4)
        print("Add product to Cart successfully!")

    def add_P5_to_cart(self):
        self._click(self.BTN_Product_5)
        print("Add product to Cart successfully!")  

    def add_P6_to_cart(self):
        self._click(self.BTN_Product_6)
        print("Add product to Cart successfully!")

    def Goto_Cart(self):
        self._click(self.Cart_locator)

    def Count_item_onCart(self):
        count_items = self._return_count(self.Cart_count)
        print(f"Số lượng sản phẩm trên giỏ hàng là {count_items}")
        
