from playwright.sync_api import Page, expect
import re

def test_login(page: Page):
    print("Navigate to page Swag Labs...")
    # 1️⃣ Truy cập vào trang web yêu thích
    url = "https://www.saucedemo.com/"
    expect_title = "Swag Labs"
    page.goto(url)

    page.get_by_placeholder("Username").fill("standard_user")
    page.get_by_placeholder("Password").fill("secret_sauce")
    # password = page.get_by_placeholder("Password")
    # password.fill("secret_sauce")
    page.get_by_role("button", name="Login").click()

    expect(page.get_by_text("Products")).to_be_visible()
    print("✅ Đăng nhập thành công! Hiển thị trang với tiêu đề 'Products' ")

    # 6️⃣ Đếm số lượng sản phẩm hiển thị trên trang
    products = page.locator(".inventory_item")
    count = products.count()
    print(f"🛒 Số lượng sản phẩm hiển thị: {count}")


