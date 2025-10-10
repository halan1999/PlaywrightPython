# Viết file mới test_bai_tap.py để:
# 1️⃣ Truy cập vào trang web yêu thích (ví dụ: shopee.vn, vnexpress.net, công ty bạn).
# 2️⃣ Kiểm tra tiêu đề trang có đúng mong đợi.
# 3️⃣ Kiểm tra URL trang web.


from playwright.sync_api import Page, expect
import re, time

def test_title_and_page_url(page: Page):
    print("Opening Google Chrome browser...")
    page.goto("https://www.parcelperform.com/")
    time.sleep(5)
    
    # Verify title
    expect(page).to_have_title("Parcel Perform | AI Delivery Experience SaaS Software")
    print("Title is correct: Parcel Perform | AI Delivery Experience SaaS Software")
    
    # Verify URL
    expect(page).to_have_url("https://www.parcelperform.com/")
    print("URL is correct: https://www.parcelperform.com/")
