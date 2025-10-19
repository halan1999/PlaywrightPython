# from playwright.sync_api import Page, expect
# import re, time

# def test_check_title_page(page: Page):
#     print(f"truy cập trang web")
#     #truy cập trang web
#     page.goto("https://www.thegioididong.com/")
#     #kiểm tra xem có tiêu đề không
#     expect(page).to_have_title(re.compile("Thegioididong"))
#     print(f"tiêu đề đã đúng là Thegioididong")
#     #kiểm tra xem url có chứa cụm từ không
#     expect(page).to_have_url(re.compile("thegioididong"))
#     print(f"URL hợp lệ")
#     time.sleep(5)

from playwright.sync_api import Page, expect
import re, time
def test_login(page: Page):
    print("truy cập url")
    #truy cập vào URL
    page.goto("https://www.saucedemo.com/")
    #dùng get_by_placeholder để lấy Username, Password, get_by_role để lấy login button
    page.get_by_placeholder("Username").fill("standard_user")
    page.get_by_placeholder("Password").fill("secret_sauce")
    page.get_by_role("button", name="login").click()
    # dùng ID để lấy Username, Password, login button
    page.locator("#user-name").fill("locked_out_user")
    page.locator("#password").fill("secret_sauce")
    page.locator("#login-button").click()
    # dùng thuộc tính để lấy Username, password, login button
    page.locator("[name='user-name']").fill("performance_glitch_user")
    page.locator("[name='password']").fill("secret_sauce")
    page.locator("[type='submit']").click()
    # dùng xpath để lấy username, password, login button
    page.locator("//input[contains(@data-test, 'username')]").fill("error_user")
    page.locator("//input[contains(@data-test, 'password')]").fill("secret_sauce")
    page.locator("//input[contains(@id, 'login-button')]").click()
    # dùng quan hệ cha-con để lấy username, password
    page.locator("div.form_group > input[name='user-name']").fill("visual_user")
    page.locator("div.form_group > input[name='password']").fill("secret_sauce")
    # dùng class để lấy username, password
    page.locator(".form_group input[data-test='username']").fill("standard_user")
    page.locator(".form_group input[data-test='password']").fill("secret_sauce")
    page.get_by_role("button", name="login").click()
    expect(page.get_by_text("Products")).to_be_visible()
    products = page.locator(".inventory_item")
    counts = products.count
    print(f"số lượng sản phẩm là {counts}")
    time.sleep(5)




    
