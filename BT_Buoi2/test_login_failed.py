# Cũng tại trang trên (https://www.saucedemo.com/), cố tình nhập sai password.
# Click nút Login.
# Sử dụng page.locator("[data-test='error']") kết hợp với expect().to_contain_text() để chờ và xác minh thông báo lỗi "Username and password do not match" xuất hiện.

from playwright.sync_api import sync_playwright, expect
import re

def test_login_failed(page):
    page.goto("https://www.saucedemo.com/")

    page.get_by_placeholder("Username").fill("standard_user")
    page.get_by_placeholder("Password").fill("revealed_sauce")

    page.get_by_role("button", name = "Login").click()

    error_msg = page.locator("[data-test='error']")
    expect(error_msg).to_contain_text("Username and password do not match")
    print("Error message is visible on the page")