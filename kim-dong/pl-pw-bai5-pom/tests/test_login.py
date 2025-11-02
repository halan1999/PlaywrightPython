import sys
import os
import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from playwright.sync_api import Page
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

@pytest.fixture
def test_logged_in_page(page: Page):
       # --- PHẦN 1: SETUP --- Fixture to login and return Inventory, along with Teardown logout
    print("\n[Setup] Login ...")
    login_page = LoginPage(page)
    inventory_page = login_page.login("standard_user", "secret_sauce")
    inventory_page.assert_login_successful()
    print("[Setup] Done login")

    # --- PHẦN 2: YIELD ---
    yield inventory_page

    # --- PHẦN 3: TEARDOWN ---
    print("\n[Fixture Teardown] Logging out ...")
    login_page = inventory_page.logout()
    print("[Fixture Teardown] Done logout")

def test_successful_login_standard_user(test_logged_in_page):
    assert test_logged_in_page is not None

def test_login_failure_locked_user(page):
    #from playwright.sync_api import sync_playwright

    # with sync_playwright() as p:
    #     browser = p.chromium.launch(headless=False)
    #     page = browser.new_page()

        login_page = LoginPage(page)
        login_page.login("locked_out_user", "secret_sauce")

        expected_message = "Epic sadface: Sorry, this user has been locked out."
        login_page.assert_error_message_visible(expected_message)