from playwright.sync_api import Page, expect
import re, time

def test_check_title_page(page: Page):
    print(f"truy cập trang web")
    #truy cập trang web
    page.goto("https://www.thegioididong.com/")
    #kiểm tra xem có tiêu đề không
    expect(page).to_have_title(re.compile("Thegioididong"))
    print(f"tiêu đề đã đúng là Thegioididong")
    #kiểm tra xem url có chứa cụm từ không
    expect(page).to_have_url(re.compile("thegioididong"))
    print(f"URL hợp lệ")
    time.sleep(5)