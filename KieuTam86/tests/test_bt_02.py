from playwright.sync_api import Page, expect
import re

def test_login_fail(page:Page):
    url = "https://www.saucedemo.com/"
    # expect_title = "Swag Labs"
    page.goto(url)

    page.get_by_placeholder("Username").fill("abcd")
    page.get_by_placeholder("Password").fill("123456")
    page.get_by_role("button", name="Login").click()

    expect(page.locator("[data-test='error']")).to_contain_text("Epic sadface: Username and password do not match any user in this service")
    print("Login fail username/password")