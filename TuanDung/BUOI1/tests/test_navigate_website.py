from playwright.sync_api import Page, expect
import re,time

def test_check_title_google(page : Page):
    print("Navigate to Google page...")
    page.goto("https://anhtester.com/")
    time.sleep(3)
    expect(page).to_have_title(re.compile("Anh Tester Automation Testing"))
    print("Correct title is Google")