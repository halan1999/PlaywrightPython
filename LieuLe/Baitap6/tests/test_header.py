from playwright.sync_api import sync_playwright
from ..components.header_component import HeaderComponent
from ..pages.login_page import LoginPage 

def test_header_click_screenshot():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        login_page = LoginPage(page, "LieuLe/Baitap6/data/credentials.json")
        username, password = login_page.load_credentials("valid")
        login_page.login()
        header = HeaderComponent(page)
        
        page.goto("https://hrm.anhtester.com/erp/desk")
        
        locators = [
            ("account_setting", header.account_setting),
            ("apps", header.apps),
            ("system_calendar", header.system_calendar),
            ("system_report", header.system_report),
            ("language", header.language),
            ("todo_list", header.todo_list),
            ("user_avtar", header.user_avtar),
            ("logout_list", header.logout_list)
        ]
        
        for name, locator in locators:
            try:
                print(f"Clicking: {name}")
                page.locator(locator).click()
                header._take_screenshot(f"{name}.png")
            except Exception as e:
                print(f"Cannot click {name}: {e}")
        
        browser.close()
    