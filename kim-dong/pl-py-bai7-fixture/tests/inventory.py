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


def test_add_random_product_to_cart():
    from playwright.sync_api import sync_playwright

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://www.saucedemo.com")

        # Login
        login_page = LoginPage(page)
        login_page.login("standard_user", "secret_sauce")

        inventory = InventoryPage(page)
        selected = inventory.add_random_product_to_cart()
        inventory.go_to_cart()
        inventory.assert_product_in_cart(selected)

        browser.close()

if __name__ == "__main__":
    test_add_to_cart_after_login()
    test_add_random_product_to_cart()
