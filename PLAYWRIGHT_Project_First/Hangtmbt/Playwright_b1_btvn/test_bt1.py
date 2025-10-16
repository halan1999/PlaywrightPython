from playwright.sync_api import Page, expect
import re
import time
def test_open_page(page:Page):
    page.goto("https://anhtester.com/")
    expect(page).to_have_title(re.compile("Anh Tester Automation Testing"))
    print("Test case 1: Mở trang VnExpress")
    expect(page).to_have_url(re.compile("https://anhtester.com/"))
    print("Test case 2: Kiểm tra URL")
    
