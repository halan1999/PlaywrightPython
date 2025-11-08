from pages.login_page import LoginPage
from components.header_component import header_component
import json
from playwright.sync_api import Page

def test_login_with_valid_credentials(page: Page):
    login_page = LoginPage(page)
    
    with open("/Users/ducnt/PlaywrightPython/Ducnt/my-playwright-project/data/scredentials.json") as f:
        creds = json.load(f)

    valid = creds["valid_user"]
    login_page.login(valid["username"], valid["password"])
    login_page.assert_login_successful()
    header = header_component(page)
    header.click_and_screenshot_header()
    login_page.logout()
    login_page.assert_logout_successful()