from playwright.sync_api import Locator
from pages.base_page import BasePage

class InventoryPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.product = []
    
    def add_to_cart(self, product_name : str):
        Xpath_lbl_product_name = f'//div[normalize-space()="{product_name}"]'
        Xpath_lbl_product_detail = f'{Xpath_lbl_product_name}/parent::a/following-sibling::div'
        Xpath_product_price = f'{Xpath_lbl_product_name}/ancestor::div[@class="inventory_item_label"]/following-sibling::div//div'
        Xpath_btn_add_to_cart = f'{Xpath_lbl_product_name}/ancestor::div[@class="inventory_item_label"]/following-sibling::div//button'
        
        locator_detail = self.page.locator(Xpath_lbl_product_detail)
        locator_price = self.page.locator(Xpath_product_price)
        product = self.__get_detail_product(product_name, locator_detail, locator_price)

        self.page.locator(Xpath_btn_add_to_cart).click()

        self.product.append(product)

    def __get_detail_product(product_name : str, locator_detail: Locator, locator_price: Locator):
        dict_product = {"name" : "", "detail" : "", "price" : ""}
        dict_product["name"] = product_name
        dict_product["detail"] = locator_detail.inner_text()
        dict_product["price"] = locator_price.inner_text()

        return dict_product


    def assert_login_pass(self):
        super()._verify_home_page_visible()