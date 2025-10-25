from playwright.sync_api import Page, expect
import re
def test_login_fail(page: Page):
    
    url = "https://www.saucedemo.com/"
    # Truy cập vào trang https://www.saucedemo.com/
    page.goto("https://www.saucedemo.com/")
    # Kiểm tra tiêu đề trang có đúng mong đợi.
    expect(page).to_have_title(re.compile("Swag Labs"))
    # Sử dụng page.get_by_placeholder("Username") để điền standard_user
    page.get_by_placeholder("Username").fill("standard_user")
    # Sử dụng page.get_by_placeholder("Password") để điền sai mật khẩu
    page.get_by_placeholder("Password").fill("wrong_password_1")
    # Sử dụng page.get_by_role("button", name="Login") để click vào nút Login
    page.get_by_role("button", name="Login").click()
    # Sử dụng page.locator("[data-test='error']") 
    expect(page.locator("[data-test='error']")).to_contain_text("Username and password do not match")
    print("Thông báo lỗi xuất hiện như mong đợi: Username and password do not match")