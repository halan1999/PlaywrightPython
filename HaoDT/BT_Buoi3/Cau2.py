import pytest
from playwright.sync_api import Page, expect

def test_click_red_button(page: Page):
    #Truy cập trang
    page.goto("https://the-internet.herokuapp.com/challenging_dom")

    #Refactor locator ổn định — chọn nút màu đỏ
    red_button = page.locator("a.button.alert")

    #Click vào nút
    red_button.click()

    #Xác nhận nút vẫn hiển thị sau khi click
    expect(red_button).to_be_visible()
