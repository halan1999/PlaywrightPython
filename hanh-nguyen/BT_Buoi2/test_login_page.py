# Truy cập trang https://www.saucedemo.com/
# Sử dụng page.get_by_placeholder("Username") để điền standard_user.
# Sử dụng page.get_by_placeholder("Password") để điền secret_sauce.
# Click nút Login bằng page.get_by_role("button", name="Login").
# Dùng expect để chờ và xác nhận tiêu đề "Products" xuất hiện: expect(page.get_by_text("Products")).to_be_visible().
# In ra số lượng sản phẩm có trên trang (gợi ý: locator là .inventory_item).

from playwright.sync_api import sync_playwright, expect
import re

def test_enter_page_saucedemo(page):
    page.goto("https://www.saucedemo.com/")

    page.get_by_placeholder("Username").fill("standard_user")
    page.get_by_placeholder("Password").fill("secret_sauce")

    page.get_by_role("button", name = "Login").click()

    expect(page.get_by_text("Products")).to_be_visible()
    print("'Products' text is visible on the page")

    products = page.locator(".inventory_item")
    products_count = products.count()
    print(f"The number of product on the page is: {products}")

