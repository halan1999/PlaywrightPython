import pytest
from playwright.sync_api import sync_playwright

def test_trang_web_yeu_thich():
    # URL trang web yêu thích (bạn có thể đổi sang trang khác)
    expected_url = "https://shopee.vn/"
    expected_title_keyword = "Shopee"   # Kiểm tra tiêu đề có chứa từ này

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # headless=True để chạy ẩn
        page = browser.new_page()
        
        # 1️⃣ Truy cập vào trang web
        page.goto(expected_url)
        
        # 2️⃣ Kiểm tra tiêu đề trang
        title = page.title()
        print(f"Tiêu đề trang: {title}")
        assert expected_title_keyword.lower() in title.lower(), "❌ Tiêu đề không đúng mong đợi"
        
        # 3️⃣ Kiểm tra URL hiện tại
        current_url = page.url
        print(f"URL hiện tại: {current_url}")
        assert current_url.startswith(expected_url), "❌ URL không khớp mong đợi"
        
        browser.close()
