import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
sys.stdout.reconfigure(line_buffering=True)

import pytest
from pages.login_page import LoginPage
from playwright.sync_api import Page, expect

@pytest.fixture
def test_logged_in_page(page: Page):
    # --- PHẦN 1: SETUP ---
    print("\n[Setup] Login ...")
    login_page = LoginPage(page)
    secure_area_page = login_page.login("tomsmith", "SuperSecretPassword!")
    expect(secure_area_page.flash_message).to_contain_text("You logged into a secure area!")
    print("[Setup] Done login")

    # --- PHẦN 2: YIELD ---
    yield secure_area_page

    # --- PHẦN 3: TEARDOWN ---
    print("\n[Fixture Teardown] Logging out ...")
    login_page = secure_area_page.logout()
    #print("[DEBUG] logout type:", type(login_page.logout))
    expect(login_page.flash_message).to_contain_text("You logged out of the secure area!")
    print("[Fixture Teardown] Done logout")

def test_login_success(test_logged_in_page):
    # Kiểm tra xem người dùng đã đăng nhập thành công chưa
    print("[Test] Checking Secure Page")
    #print(">>>>>>> TYPE:", type(test_logged_in_page))
    try:
        expect(test_logged_in_page.page.locator("h2")).to_have_text("Secure Area")
        
    except AssertionError as e:
        print("❌ FAIL:", e)
        raise  # vẫn raise để pytest báo test fail