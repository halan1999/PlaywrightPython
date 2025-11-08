from playwright.sync_api import Page, expect
import re
def test_count_products(page: Page):
    

    print("Navigate to Saucedemo page...")
    url = "https://www.saucedemo.com/"
    # Truy cập vào trang https://www.saucedemo.com/
    page.goto("https://www.saucedemo.com/")
    # Kiểm tra tiêu đề trang có đúng mong đợi.
    expect(page).to_have_title(re.compile("Swag Labs"))
    # Sử dụng page.get_by_placeholder("Username") để điền standard_user
    page.get_by_placeholder("Username").fill("standard_user")
    # Sử dụng page.get_by_placeholder("Password") để điền secret_sauce
    page.get_by_placeholder("Password").fill("secret_sauce")
    # Sử dụng page.get_by_role("button", name="Login") để click vào nút Login
    page.get_by_role("button", name="Login").click()
    # Dùng expect để chờ và xác nhận tiêu đề "Products" xuất hiện
    expect(page.get_by_text("Products")).to_be_visible()
    # In ra số lượng sản phẩm có trên trang (gợi ý: locator là .inventory_item).
    products = page.locator(".inventory_item")
    print("Số lượng sản phẩm trên trang:", products.count())
