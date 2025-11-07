import json

from BT_BUOI8.pages.login_page import LoginPage
from BT_BUOI8.pages.inventory_page import InventoryPage

def test_add_to_cart(page):
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)

    # Login
    with open("BT_BUOI8/data/users.json") as f:
        user = json.load(f)

    valid = user["valid_user"]

    login_page.login(valid["username"], valid["password"])
    login_page.assert_login_successful()

    # Add product
    inventory_page.add_item_to_cart(['backpack', 'bike-light', 'bolt-t-shirt', 'fleece-jacket', 'onesie'])

    # Assert number of item
    assert inventory_page.assert_cart_badge_count("5")

