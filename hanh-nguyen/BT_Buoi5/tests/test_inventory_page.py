from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

def test_add_then_remove_highest_price_product(page):
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)

    login_page.login("standard_user", "secret_sauce")
    login_page.assert_login_successful()

    inventory_page.click_product_filter()
    inventory_page.filter_by_highest_price()

    inventory_page.add_to_cart()
    inventory_page.assert_cart_badge_count("1")

    inventory_page.remove_product()
    inventory_page.assert_cart_badge_count_not_visible()
