from playwright.sync_api import sync_playwright
from ..components.left_component import LeftComponent
from ..pages.login_page import LoginPage 

def test_scroll_left_menu ():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        login_page = LoginPage(page, "LieuLe/Baitap6/data/credentials.json")
        username, password = login_page.load_credentials("valid")
        login_page.loginwith()
        left_menu = LeftComponent(page)
        page.goto("https://hrm.anhtester.com/erp/desk")
        login_page.take_before_scroll_screenshot(left_menu.left_menu1,"before_scroll_left_menu.png")
        left_menu.take_after_scroll_screenshot(left_menu.left_menu1,"after_scroll_left_menu.png")
        browser.close()