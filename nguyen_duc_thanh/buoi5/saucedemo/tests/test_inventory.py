from buoi5.pages.inventory_page import InventoryPage
from buoi5.pages.login_page import LoginPage


def test_add_to_cart(page):
    login_page = LoginPage(page)
    login_page.login("standard_user", "secret_sauce")
    login_page.assert_login_successful()
    inventory_page = InventoryPage(page)
    inventory_page._add_to_cart_backpack()
    inventory_page._verify_backpack_is_added("1")