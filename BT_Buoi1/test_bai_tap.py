# Viết file mới test_bai_tap.py để:
# 1️⃣ Truy cập vào trang web yêu thích (ví dụ: shopee.vn, vnexpress.net, công ty bạn).
# 2️⃣ Kiểm tra tiêu đề trang có đúng mong đợi.
# 3️⃣ Kiểm tra URL trang web.

import re
from playwright.sync_api import Page, expect

def test_kiem_tra_tieu_de_linkedin(page: Page):
    print("Open Linkedin page...")

    page.goto("https://www.linkedin.com/")

    expect(page).to_have_title(re.compile("LinkedIn: Log In or Sign Up"))
    print("Correct title!")

    expect(page).to_have_url(re.compile("https://www.linkedin.com/"))
    print("Correct URL!")