import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from playwright.sync_api import sync_playwright
from playwright.sync_api import Page, expect

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

def test_add_to_cart_after_login():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        login_page = LoginPage(page)

        login_page = LoginPage(page)
        inventory_page = InventoryPage(page)

        login_page.login("standard_user", "secret_sauce")
        login_page.assert_login_successful()

        inventory_page.add_backpack_to_cart()
        inventory_page.assert_cart_badge_count("1")

        browser.close()


def test_add_to_product_to_cart_and_check_cart():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        login_page = LoginPage(page)

        login_page = LoginPage(page)
        inventory_page = InventoryPage(page)

        login_page.login("standard_user", "secret_sauce")

        product_name = "Sauce Labs Backpack"
        inventory_page.add_product_to_cart()
        inventory_page.assert_product_in_cart(product_name)


        browser.close()

if __name__ == "__main__":
    test_add_to_cart_after_login()
    test_add_to_product_to_cart_and_check_cart()
