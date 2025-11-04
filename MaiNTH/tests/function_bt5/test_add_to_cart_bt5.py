from playwright.sync_api import Page, Playwright, expect  # type: ignore[import]
import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


@pytest.fixture(scope="function")
def logged_in_page(playwright: Playwright):
    # Setup trước khi test run
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    # Login bằng POM
    login_page = LoginPage(page)
    login_page.visit_login_page()
    login_page.login("standard_user", "secret_sauce")

    # Đảm bảo login thành công
    expect(page).to_have_url(InventoryPage.URL)
    print("1. Login successfully")

    # Trả về page đã login cho test sử dụng
    yield page

    # Teardown
    print("Teardown: Logout and close browser")
    page.get_by_role("button", name="Open Menu").click()
    page.get_by_role("link", name="Logout").click()

    context.close()
    browser.close()


def test_add_to_cart_flow(logged_in_page: Page) -> None:
    inventory_page = InventoryPage(logged_in_page)
    # Add item 1 to cart
    inventory_page.add_item_to_cart_by_name("Sauce Labs Backpack")
    print("2. Added item 'Sauce Labs Backpack' to cart successfully")
    # Add item 2 to cart
    inventory_page.add_item_to_cart_by_name("Sauce Labs Bike Light")
    print("2. Added item 'Sauce Labs Bike Light' to cart successfully")
    # Verify item added to cart
    count = inventory_page.get_cart_count()
    expect(count).to_have_text("2")
    print("3. Verified items added to cart successfully")