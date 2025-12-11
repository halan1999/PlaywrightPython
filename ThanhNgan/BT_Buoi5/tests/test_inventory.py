from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from playwright.sync_api import expect, Page
import time
import json

def test_add_item_successfully(page):
    login_page = LoginPage(page)
    login_page.login("standard_user","secret_sauce")

    # Add item 
    btn_item_1 = "//div[@class='inventory_list']//div[@class='inventory_item'][1]//button[normalize-space()='Add to cart']"
    login_page._click(btn_item_1)
    # Add item successfully
    print("Add product successfully")
    time.sleep(2)
    # Navigate to Cart 
    inventory_page = InventoryPage(page)
    inventory_page.goto_cart()
    time.sleep(2)
    # Get the current total item
    current_total_item = inventory_page.count_item()
    if current_total_item > 0:
        print("Add item to cart successfully")

