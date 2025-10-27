from playwright.sync_api import Page, expect
import re

def test_trang_chu(page : Page):
    expected_title = "Cổng Thông tin điện tử Chính phủ"
    expected_url = "https://chinhphu.vn/"

    page.goto(expected_url)
    expect(page).to_have_title(re.compile(expected_title))
    expect(page).to_have_url(re.compile(expected_url))

    print("Testcase passed!")
