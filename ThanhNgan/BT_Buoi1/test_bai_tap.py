"""
Viết file mới test_bai_tap.py để:
1️⃣ Truy cập vào trang web yêu thích (ví dụ: shopee.vn, vnexpress.net, công ty bạn).
2️⃣ Kiểm tra tiêu đề trang có đúng mong đợi.
3️⃣ Kiểm tra URL trang web.
"""
from playwright.sync_api import Page, expect
import re

def test_check_title(page: Page):
    print("Mở trình duyệt shopee...")

    page.goto("https://www.apple.com/vn/")

    # Check title
    expect(page).to_have_title(re.compile(r'Apple \(Việt Nam\)'))
    print("Title is correct")

    # Check url 
    expect(page).to_have_url(re.compile('https://www.apple.com/vn/'))
    print("URL is correct")


