#  Truy cập vào trang https://vnexpress.net/
#  Kiểm tra tiêu đề trang có đúng mong đợi.
#  Kiểm tra URL có đúng không
import time
from playwright.sync_api import Page, expect
import re

def test_check_page_favorite(page: Page):
    print("Navigate to VnExpress page...")
    url = "https://vnexpress.net/"
    expect_title = "VnExpress - Báo tiếng Việt nhiều người xem nhất"

    # Truy cập với thời gian chờ lâu hơn và chỉ đợi DOM sẵn sàng
    page.goto(url, wait_until="domcontentloaded", timeout=100000)


    # Kiểm tra tiêu đề
    expect(page).to_have_title(re.compile(expect_title))
    print("Tiêu đề chính xác:", expect_title)

    # Kiểm tra URL
    expect(page).to_have_url(re.compile("https://vnexpress.net/"))
    print("URL chính xác:", url)
