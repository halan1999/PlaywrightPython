from playwright.sync_api import Page, expect
import re,time

# def test_login_success(page: Page):
#     page.goto('https://www.saucedemo.com/')
#     page.get_by_placeholder("Username").fill("standard_user")
#     page.get_by_placeholder("Password").fill("secret_sauce")
#     page.get_by_role("button", name="Login").click()
#     expect(page.get_by_text('Product')).to_be_visible()
#     products = page.locator(".inventory_item")
#     count = products.count()
#     print(f"✅ Tổng số sản phẩm: {count}")
#     for i in range(count):
#         name = products.nth(i).locator(".inventory_item_name").inner_text()
#         print(f"📦 Sản phẩm {i+1}: {name}")
#     time.sleep(15)

def test_login_wrongpass(page: Page):
    page.goto('https://www.saucedemo.com/')
    usernname = page.locator("//div//input[@id='user-name']")
    usernname.fill("standard_user")
    password = page.locator("//div//input[@id='password']")
    password.fill("123456")
    page.click("//input[@id='login-button']")
    expect(page.locator("//h3[@data-test='error']")).to_be_visible()
    expect(page.locator("//h3[@data-test='error']")).to_have_text("Epic sadface: Username and password do not match any user in this service")
    time.sleep(15)
