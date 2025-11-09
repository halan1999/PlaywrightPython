from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from playwright.sync_api import expect
import time

def test_login_success_standard_user(page):
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)

    login_page.login("standard_user", "secret_sauce")
    inventory_page.verify_login_success()
    print("Login successfully!")


def test_login_failure_locked_user(page):
    login_page = LoginPage(page)
    login_page.login("locked_out_user", "secret_sauce")
    login_page.assert_error_message_visible()
    
def test_login_problem(page):
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)

    login_page.login("problem_user", "secret_sauce")
    inventory_page.verify_login_success()
    print("Navigations to Products page!")

def test_login_performance(page):
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)

    login_page.login("performance_glitch_user", "secret_sauce")
    inventory_page.verify_login_success()
    print("Navigations to Products page!")   

def test_login_error_user(page):
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)

    login_page.login("error_user", "secret_sauce")
    inventory_page.verify_login_success()
    print("Navigations to Products page!")   

def test_login_visual_user(page):
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)

    login_page.login("visual_user", "secret_sauce")
    inventory_page.verify_login_success()
    print("Navigations to Products page!")  

def test_Verify_items_Cart(page):

    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)
    cart_page = CartPage(page)

    login_page.login("standard_user", "secret_sauce")
    inventory_page.verify_login_success()
    print("Login successfully!")

    inventory_page.add_P1_to_cart()
    inventory_page.add_P2_to_cart()

    inventory_page.Count_item_onCart()