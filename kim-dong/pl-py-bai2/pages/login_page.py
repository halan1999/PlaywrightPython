import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


from playwright.sync_api import Page, expect

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.username_input = page.locator("#user-name")
        self.password_input = page.locator("#password")
        self.login_button = page.locator("#login-button")
        self.error_message = page.locator("[data-test='error']")
        self.product_title = page.get_by_text("Products")
        self.inventory_items = page.locator(".inventory_item")

    def navigate(self):
        self.page.goto("https://www.saucedemo.com/")

    def login(self, username: str, password: str):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()

    def verify_login_success(self):
        expect(self.product_title).to_be_visible()

    def count_products(self) -> int:
        return self.inventory_items.count()

    def verify_login_failure(self, expected_text: str):
        expect(self.error_message).to_contain_text(expected_text)
        