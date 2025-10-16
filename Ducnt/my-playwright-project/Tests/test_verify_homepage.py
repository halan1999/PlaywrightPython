from playwright.sync_api import Page, expect
import re

def test_homepage_title(page: Page):
    # Navigate to the homepage
    page.goto("https://google.com")
    expect(page).to_have_title(re.compile("Google"))
    print("Title verified successfully.")
