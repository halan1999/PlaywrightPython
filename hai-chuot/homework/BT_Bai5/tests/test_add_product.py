from playwright.sync_api import Page
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
import time

def test_add_product(page : Page):
    USERNAME = 'standard_user'
    PASSWORD = 'secret_sauce'
    PRODUCT_ADD_TO_CART = 'Sauce Labs Onesie'
    try:
        login_page = LoginPage(page)
        login_page.login(USERNAME, PASSWORD)
        login_page.assert_login_pass()
    except:
        raise ValueError('Đăng nhập không thành công với tài khoản: {USERNAME}')   
    

    inventory_page = InventoryPage(page)
    inventory_page.add_to_cart(PRODUCT_ADD_TO_CART)
    inventory_page.verify_cart()