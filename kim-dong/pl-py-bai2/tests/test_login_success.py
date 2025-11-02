import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage


def test_login_success():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        login_page = LoginPage(page)

        print("Truy cập trang....")
        login_page.navigate()
        print("Điền thông tin đăng nhập")
        login_page.login("standard_user", "secret_sauce")
        login_page.verify_login_success()

        count = login_page.count_products()
        print(f"Số lượng sản phẩm: {count}")
        assert count > 0

        browser.close()

if __name__ == "__main__":
    test_login_success()
