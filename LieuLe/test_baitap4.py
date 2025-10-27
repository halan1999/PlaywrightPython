import pytest
from playwright.sync_api import Page
import time
import sys
import pytest
from playwright.sync_api import sync_playwright
URL = " https://hrm.anhtester.com/erp/login"
Usename = "admin_example"
Pass = "123456"
Login_button = "button[type='login']"
def test_run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        page.goto(URL)
        page.locator ("#iusername").fill(Usename)
        page.locator("#ipassword").fill(Pass)
        page.click("//button[@type='submit' and contains(., 'Login')]")
        time.sleep(3)
        #print("Login button has been clicked:", page.url)
        page.click("//a[contains(., 'Core HR')]")
        #page.click("//a[contains(@class,'pc-link') and normalize-space()='Department']")
        page.click("a.pc-link:has-text('Department')")
        #page.get_by_placeholder("Name").fill("Accounting Department")
        page.fill("input[name='department_name']", "Accounting Deparment")
        page.click("//button[@type='submit' and contains(.,'Save')]")

        print(page.content()) 
        browser.close()

if __name__ == "__main__":
    test_run()