from pages.login_page import LoginPage
from pages.inven_page import Inventory_page
from playwright.sync_api import expect

def add_to_cart_after_login(page):
    login_page = LoginPage(page)
    login_page.login("standard_user", "secret_sauce")
    login_page.assert_login_successful()
    inventory_page = Inventory_page(page)
    inventory_page.add_to_cart()
    


