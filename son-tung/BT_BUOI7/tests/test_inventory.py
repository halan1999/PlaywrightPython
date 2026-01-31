from BT_BUOI7.pages.login_page import LoginPage
from BT_BUOI7.pages.inventory_page import InventoryPage

def test_add_to_cart(page):
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)

    # Open webpage and login
    login_page.goto()
    login_page.login("standard_user", "secret_sauce")
    login_page.assert_login_successful()

    # Add product
    inventory_page.add_item_to_cart(['backpack', 'bike-light', 'bolt-t-shirt', 'fleece-jacket', 'onesie'])

    # Assert number of item
    assert inventory_page.assert_cart_badge_count("5")

