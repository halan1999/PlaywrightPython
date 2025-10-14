# Cũng tại trang trên, cố tình nhập sai password.
# Click nút Login.
# Sử dụng page.locator("[data-test='error']") kết hợp với expect().to_contain_text() để chờ và xác minh thông báo lỗi "Username and password do not match" xuất hiện.

from playwright.sync_api import Page, expect
import re, time

def test_login_success(page: Page):
     page.goto(" https://www.saucedemo.com/")

     # Find username and password field
     usernameField = page.get_by_placeholder("Username").fill("standard_user")
     passwordField = page.get_by_placeholder("Password").fill("secret_sauce123")
     loginButton = page.get_by_role("button", name="Login").click()

     expect(page.locator("[data-test='error']")).to_contain_text("Username and password do not match")

     print("Invalid credentials, login failed")

     productCount = page.locator(".inventory_item").count()
     print(f"Inventory: {productCount}")
     
     page.wait_for_timeout(5000)