from playwright.sync_api import Page, expect
import re, time

def test_addtocart(page: Page):
    page.goto("https://www.saucedemo.com/")
    page.locator("//div//input[@id='user-name']").fill("standard_user")
    page.locator("//div//input[@id='password']").fill("secret_sauce")
    page.click("//input[@id='login-button']")
    page.locator("//div[@data-test='inventory-item-name']").first.click()
    page.locator("//div//button[@id='add-to-cart']").click()
    expect(page.locator("//div//button[@id='remove']")).to_have_text("Remove")
    time.sleep(15)

