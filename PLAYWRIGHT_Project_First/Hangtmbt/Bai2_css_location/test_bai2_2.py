from playwright.sync_api import Page, expect
import re
def test_open_page(page:Page):
    page.goto("https://www.saucedemo.com/")
    page.get_by_placeholder("Username").fill("standard_user")
    page.get_by_placeholder("Password").fill("secret")
    page.get_by_role("button", name="Login").click()
    error= page.locator("[data-test='error']")
    expect(error).to_be_visible()
    expect(error).to_have_text("Username and password do not match")