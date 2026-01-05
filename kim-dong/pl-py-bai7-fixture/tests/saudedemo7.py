import pytest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from playwright.sync_api import sync_playwright

from pages.login_page import LoginPage
from playwright.sync_api import Page, expect

@pytest.fixture
def logged_in_page(page: Page):
    # --- PHẦN 1: SETUP ---
    print("\n[Fixture Setup]: Đang đăng nhập...")
    login_page = LoginPage(page)
    login_page.login("tomsmith", "SuperSecretPassword!")
    expect(login_page.flash_message).to_contain_text("You logged in!")
    
    # --- PHẦN 2: YIELD ---
    # Giao 'page' (đã đăng nhập) cho test case
    yield page
    
    # --- PHẦN 3: TEARDOWN (Chạy sau test) ---
    print("\n[Fixture Teardown]: Đang đăng xuất...")
    page.get_by_role("link", name="Logout").click()
    expect(page.locator("#flash")).to_contain_text("You logged out!")
    