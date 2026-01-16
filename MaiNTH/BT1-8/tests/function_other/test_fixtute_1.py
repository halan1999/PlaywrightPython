import re
import pytest
from playwright.sync_api import Page, Playwright, sync_playwright, expect
@pytest.fixture (scope="function")
def logged_in_page (playwright: Playwright) -> Page:
    # 1.Setup trước khi test run
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    # Go to https://hrm.anhtester.com/erp/login
    page.goto("https://www.saucedemo.com/")
    page.get_by_role("textbox", name="Username").click().fill("standard_user")
    page.get_by_role("textbox", name="Password").click().fill("secret_sauce")
    page.get_by_role("button", name=" Login").click()
    # Đảm bảo loin thành công
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
    print("1.Login successfully")
    # 2. Trả về page đã login để test sử dụng
    yield page
    # 3. Teardown sau khi test kết thúc
    print("Teardown: Logout and close browser")
    page.locator("//div[@class='primary_header']").click()
    page.get_by_role("link", name="Logout").click()
    context.close()
    browser.close()
def test_add_to_cart_flow(logged_in_page: Page) -> None:
    # Add item to cart
    logged_in_page.get_by_role("button", name="Add to cart").first.click()
    print("2. Added item to cart successfully")
    # Verify item added to cart
    cart_count = logged_in_page.locator("//span[@class='shopping_cart_badge']")
    expect(cart_count).to_have_text("1")
    print("3. Verified item added to cart successfully")

    # test_view_product_details_flow(logged_in_page: Page) -> None:
def test_view_product_details_flow(logged_in_page: Page) -> None:
    # View product details
    logged_in_page.get_by_role("link", name="Sauce Labs Backpack").click()
    print("2. Viewed product details successfully")
    # Verify product details page
    expect(logged_in_page).to_have_url(re.compile("https://www.saucedemo.com/inventory-item.html?id=4"))
    print("3. Verified product details page successfully")
   