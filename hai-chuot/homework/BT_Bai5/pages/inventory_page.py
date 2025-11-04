from playwright.sync_api import Locator
from pages.base_page import BasePage

class InventoryPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.lst_product = []
    
    def add_to_cart(self, product_name : str):
        Xpath_lbl_product_name = f'//div[normalize-space()="{product_name}"]'
        Xpath_lbl_product_detail = f'{Xpath_lbl_product_name}/parent::a/following-sibling::div'
        Xpath_product_price = f'{Xpath_lbl_product_name}/ancestor::div[@class="inventory_item_label"]/following-sibling::div//div'
        Xpath_btn_add_to_cart = f'{Xpath_lbl_product_name}/ancestor::div[@class="inventory_item_label"]/following-sibling::div//button'
        
        locator_detail = self.page.locator(Xpath_lbl_product_detail).inner_text()
        locator_price = self.page.locator(Xpath_product_price).inner_text()
        product = self.__get_detail_product(product_name, locator_detail, locator_price)

        self.page.locator(Xpath_btn_add_to_cart).click()

        self.lst_product.append(product)

    def __get_detail_product(self, product_name : str, locator_detail: str, locator_price: str) -> dict:
        dict_product = {"name" : "", "detail" : "", "price" : ""}
        dict_product["name"] = product_name
        dict_product["detail"] = locator_detail
        dict_product["price"] = locator_price

        return dict_product
    
    def verify_cart(self):
        self._click_cart()

        for product in self.lst_product:
            Xpath_item_name = f'//div[@class="inventory_item_name" and normalize-space()="{product["name"]}"]'
            Xpath_item_detail =  f'{Xpath_item_name}/parent::a/following-sibling::div[@class="inventory_item_desc"]'
            Xpath_item_price = f'{Xpath_item_name}/following::div[@class="inventory_item_price"]'

            actual_detail_product = self.page.locator(Xpath_item_detail).inner_text()
            actual_price_product = self.page.locator(Xpath_item_price).inner_text()

            assert actual_detail_product == product["detail"] and actual_price_product == product["price"]