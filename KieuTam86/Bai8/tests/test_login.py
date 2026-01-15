from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from components.header_component import HeaderComponent
from components.your_apps_component import YourApps
from playwright.sync_api import expect
import time, json

def test_form_logins_dispay(login_page):
    login_page.check_form_login()

def test_login_success(login_page):
    login_page.login_valid_user()

def test_login_fail_username(login_page):
    login_page.login_fail_username()

def test_login_fail_password(login_page):
    login_page.login_fail_password()

def test_login_short_password(login_page):
    login_page.login_password_short()

def test_forgot_password(login_page):
    login_page.goto_forgot_password()

def test_click_all_header_menu(logged_in_page):
      header = HeaderComponent(logged_in_page)
      header.click_all_header_items()

def test_logout_success(logged_in_page):
    header = HeaderComponent(logged_in_page)
    header.logout_by_button()

def test_click_all_Your_Apps_menu(logged_in_page):
     your_apps = YourApps(logged_in_page)
     your_apps.click_all_your_company_menu()

def test_logout_on_profile(logged_in_page):
    header = HeaderComponent(logged_in_page)
    header.logout_on_profile()
