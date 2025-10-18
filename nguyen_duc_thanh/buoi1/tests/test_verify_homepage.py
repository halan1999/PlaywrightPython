from playwright.sync_api import Page,expect
import re, time

def test_verify_homepage(page: Page):
    print("Navigate to Google")
    page.goto("https://shopee.vn/")
    time.sleep(4)
    expect(page).to_have_title(re.compile("Shopee Việt Nam | Mua sắm Online"))
    print("Correct title: Shopee Việt Nam | Mua sắm Online")

