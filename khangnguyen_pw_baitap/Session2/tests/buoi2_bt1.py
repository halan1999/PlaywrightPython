# Truy cập trang https://www.saucedemo.com/
# Sử dụng page.get_by_placeholder("Username") để điền standard_user.
# Sử dụng page.get_by_placeholder("Password") để điền secret_sauce.
# Click nút Login bằng page.get_by_role("button", name="Login").
# Dùng expect để chờ và xác nhận tiêu đề "Products" xuất hiện: expect(page.get_by_text("Products")).to_be_visible().
# In ra số lượng sản phẩm có trên trang (gợi ý: locator là .inventory_item).

from playwright.sync_api import Page, expect
import re, time

def test_login_success(page: Page):
     page.goto(" https://www.saucedemo.com/")

     # Find username and password field

     # Locators
     usernameId = page.locator("#user-name").fill("standard_user")
     passwordId = page.locator("#password").fill("secret_sauce")
     loginId = page.locator("login-button").click()

     # Xpath
     usernameXpath = page.locator("//div//input[@id='user-name']").fill("standard_user")
     passwordXpath = page.locator("//div//input[@id='password']").fill("secret_sauce")
     loginXpath = page.locator("//div//input[@id='login-button']").click()

     # Get by placeholder
     usernameField = page.get_by_placeholder("Username").fill("standard_user")
     passwordField = page.get_by_placeholder("Password").fill("secret_sauce")
     loginButton = page.get_by_role("button", name="Login").click()

     expect(page.get_by_text("Products")).to_be_visible()
     print("Login successful, Products page is opened")

     productCount = page.locator(".inventory_item").count()
     print(f"Inventory: {productCount}")
     
     page.wait_for_timeout(5000)
     





