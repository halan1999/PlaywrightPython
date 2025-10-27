from playwright.sync_api import Page, expect
import re
def test_open_page(page:Page):
    page.goto("https://www.saucedemo.com/")
    page.get_by_placeholder("Username").fill("standard_user")
    page.get_by_placeholder("Password").fill("secret_sauce")
    page.get_by_role("button", name="Login").click()
    expect(page.get_by_text("Products")).to_be_visible()
    items = page.locator(".inventory_item")
    expect(items).to_have_count(6)
    items_count=items.count()
    print("Số lượng sản phẩm hiển thị là:",items_count)
