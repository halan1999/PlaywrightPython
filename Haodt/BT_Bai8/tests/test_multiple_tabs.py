from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage
from pages.multiple_page import SocialPage
import time

def test_multiple_tabs():

    with sync_playwright() as pw:
        browser = pw.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        login = LoginPage(page)
        login.goto()
        time.sleep(6)


        # social icons
        icons = login.get_all_social_icons()

        # store tabs đã mở
        tabs = []

        # --- Click tab ---
        count = icons.count()
        for i in range(count):
            with context.expect_page() as new_tab_info:
                icons.nth(i).click()
            new_page = new_tab_info.value
            tabs.append(new_page)
            time.sleep(10)
        
        expected_text = [
        "Sign in to see who you already know at OrangeHRM",
        "See more from OrangeHRM - World's Most Popular Opensource HRIS | Secaucus NJ",
        "OrangeHRM",
        "OrangeHRM Inc"
        ]

        for idx, tab in enumerate(tabs):
           tab.bring_to_front()
           social = SocialPage(tab)
           social.verify_heading(expected_text[idx])
        # --- Back login ---
        page.bring_to_front()

        # close
        browser.close()
