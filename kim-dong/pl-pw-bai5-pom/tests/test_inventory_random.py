import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from playwright.sync_api import sync_playwright
from playwright.sync_api import Page, expect

from pages.login_page import LoginPage
from pages.inventory_random import InventoryRandom

def test_add_random_product_to_cart():
    from playwright.sync_api import sync_playwright

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://www.saucedemo.com")

        # Login
        page.fill("#user-name", "standard_user")
        page.fill("#password", "secret_sauce")
        page.click("#login-button")

        inventory = InventoryRandom(page)
        selected = inventory.add_random_product_to_cart()
        inventory.go_to_cart()
        inventory.assert_product_in_cart(selected)

        browser.close()

if __name__ == "__main__":
    test_add_random_product_to_cart()
