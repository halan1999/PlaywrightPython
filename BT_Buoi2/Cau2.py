from playwright.sync_api import Page, expect

def test_login_fail(page:Page):
        page.goto("https://www.saucedemo.com/")

        # Nhập sai mật khẩu
        page.get_by_placeholder("Username").fill("standard_user")
        page.get_by_placeholder("Password").fill("wrong_password")

        # 2. Click nút Login
        page.get_by_role("button",name="Login").click()

        # 3. Xác minh thông báo lỗi xuất hiện
        error_message = page.locator("[data-test='error']")
        expect(error_message).to_contain_text("Username and password do not match")
        print("Test xong case này rồi")
