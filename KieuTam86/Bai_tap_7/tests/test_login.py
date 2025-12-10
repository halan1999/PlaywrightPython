from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from components.header_component import HeaderComponent
from playwright.sync_api import expect
import time, json

def test_login_flow(login_page):
    login_page.login_valid_user()
    login_page.run_header_flow()

def test_login_fail_flow(login_page):
    login_page.login_fail()