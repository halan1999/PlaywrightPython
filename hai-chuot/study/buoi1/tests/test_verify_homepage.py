import re, time
from playwright.sync_api import Page, expect

def test_check_title_google(page : Page):
    print("Navigate to Google Page ...")

    page.goto("https://www.google.com/")

    time.sleep(5)

    expect(page).to_have_title(re.compile("Google"))
    expect(page).to_have_title(re.compile("google"))