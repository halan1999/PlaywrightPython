from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from playwright.sync_api import expect
import time, json

def test_login_success_standard_user(page):
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)

    login_page.login_success("standard_user", "secret_sauce")
    inventory_page.verify_logo()
    print("Login successfully!")

def test_login_failure_locked_user(page):
    login_page = LoginPage(page)
    login_page.login_success("locked_out_user", "secret_sauce")
    login_page.assert_error_message_visible()
    
def test_login_problem(page):
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)

    login_page.login_success("problem_user", "secret_sauce")
    inventory_page.verify_logo()
    print("Navigations to Products page!")

def test_login_performance(page):
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)

    login_page.login_success("performance_glitch_user", "secret_sauce")
    inventory_page.verify_logo()
    print("Navigations to Products page!")   

def test_login_error_user(page):
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)

    login_page.login_success("error_user", "secret_sauce")
    inventory_page.verify_logo()
    print("Navigations to Products page!")   

def test_login_visual_user(page):
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)

    login_page.login_success("visual_user", "secret_sauce")
    inventory_page.verify_logo()
    print("Navigations to Products page!")  

def test_Verify_items_Cart(page):
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)
    cart_page = CartPage(page)

    login_page.login_success("standard_user", "secret_sauce")
    inventory_page.verify_logo()
    print("Login successfully!")

    inventory_page.add_P1_to_cart()
    inventory_page.add_P2_to_cart()

    inventory_page.Count_item_onCart()


# def test_login_from_json(page):
#     login_page = LoginPage(page)
#     inventory = InventoryPage(page)

#     with open("data/credentials.json") as f:
#         creds = json.load(f)

#     standard_user = creds["standard_user"]
#     locked_user = creds["locked_user"]
#     problem_user = creds["problem_user"]
#     performance_user = creds["performance_user"]
#     error_user = creds["error_user"]
#     visual_user = creds["visual_user"] 

#     username = standard_user["username"]
#     password = standard_user["password"]
#     print(f"***Run TC Login với username = {username} và password = {password}***")
#     login_page.login_success(username, password)
#     inventory.verify_logo()



