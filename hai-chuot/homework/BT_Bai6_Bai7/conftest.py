import pytest
from playwright.sync_api import sync_playwright

# ==================================================
# SCOPE MODULE
# Thực hiện với mỗi lần thực thi file test_***.py
# SETUP: Khởi tạo Browser không chạy headless và dùng trình duyệt chrome của nhân chrominum
# TEARDOWN: Giải phóng đối tượng Browser
# ==================================================
@pytest.fixture(scope="module")
def open_browser():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False, channel="chrome")
            
        yield browser

        browser.close()