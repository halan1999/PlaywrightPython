from playwright.sync_api import Page, expect
import re

def test_check_page_favorite(page: Page):
    print("Navigate to Shopee page...")
    # 1️⃣ Truy cập vào trang web yêu thích
    url = "https://playwright.dev/python/docs/intro"
    expect_title = "Installation | Playwright Python"
    page.goto(url)
    # 2️⃣ Kiểm tra tiêu đề trang có đúng mong đợi.
    expect(page).to_have_title(re.compile(expect_title))
    print("✅ Tiêu đề chính xác: Installation | Playwright Python")
    # 3️⃣ Kiểm tra URL có đúng không
    expect(page).to_have_url(re.compile("https://playwright.dev/python/docs/intro"))
    print("✅ Test passed – Trang web hoạt động như mong đợi!")


