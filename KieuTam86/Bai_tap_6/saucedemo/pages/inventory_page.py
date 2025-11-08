from core.base_page import BasePage
from components.header_components import HeaderComponent

class InventoryPage(BasePage):
    """Đại diện cho trang danh sách sản phẩm."""

    inventory_logo = "//div[@class ='app_logo']"
    BTN_Product_1 = "#add-to-cart-sauce-labs-backpack"
    "cách lấy khác "
    # BTN_Product_1 = "[data-test='add-to-cart-sauce-labs-backpack']"
    BTN_Product_2 = "#add-to-cart-sauce-labs-bike-light"
    # BTN_Product_2 = "[data-test='add-to-cart-sauce-labs-bike-light']"
    BTN_Product_3 = "#add-to-cart-sauce-labs-bolt-t-shirt"
    # BTN_Product_3 = "[data-test='add-to-cart-sauce-labs-bolt-t-shirt']"
    BTN_Product_4 = "#add-to-cart-sauce-labs-fleece-jacket"
    # BTN_Product_4 = "[data-test='add-to-cart-sauce-labs-bolt-t-shirt']"
    BTN_Product_5 = "#add-to-cart-sauce-labs-onesie"
    # BTN_Product_5 = "[data-test='add-to-cart-sauce-labs-onesie']"
    BTN_Product_6 = "add-to-cart-test.allthethings()-t-shirt-(red)"
    BTN_Product_6 = "[data-test='add-to-cart-test.allthethings()-t-shirt-(red)']"
    SHOPPING_CART_BADGE = "//span[@class='shopping_cart_badge']"

    def __init__(self, page):
        super().__init__(page)
        
        # Gắn Component Header vào trang
        self.header = HeaderComponent(page)    

    def verify_logo(self):
        self._verify_text(self.inventory_logo, "Swag Labs")
        self._take_screenshot(f"{self.inventory_logo}.png")

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
        self._click(self.SHOPPING_CART_BADGE)

    def Verify_Item_Added(self):
        """Kiểm tra biểu tượng giỏ hàng hiển thị số lượng đúng."""
        self._verify_visible(self.SHOPPING_CART_BADGE)

    def Count_item_onCart(self):
        count_items = self._return_count(self.SHOPPING_CART_BADGE)
        print(f"Số lượng sản phẩm trên giỏ hàng là {count_items}")

    def Logout_Via_Header(self):
        """Đăng xuất qua Header Component."""
        self.header.logout()    
        
