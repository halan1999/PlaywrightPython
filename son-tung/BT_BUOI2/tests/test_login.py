from playwright.sync_api import Page, expect

def test_web_login(page : Page):
        page.goto("https://www.saucedemo.com/")

# Cách 1:
        page.get_by_placeholder("Username").fill("standard_user")
        page.get_by_placeholder("Password").fill("secret_sauce")

        page.get_by_role("button", name="Login").click()

        expect(page.get_by_text("Products")).to_be_visible()
        p1 = page.locator(".inventory_item").count()

        page.locator("//button[normalize-space()='Open Menu']").click()
        page.locator("//a[normalize-space()='Logout']").click()

# Cách 2:
        page.locator("#user-name").fill("locked_out_user")
        page.locator("#password").fill("secret_sauce")

        page.locator("#login-button").click()

        expect(page.locator("[data-test='error']")).to_be_visible()

# Cách 3:
        page.locator("//input[@id='user-name']").fill("problem_user")
        page.locator("//input[@id='password']").fill("secret_sauce")

        page.locator("//input[@id='login-button']").click()

        expect(page.locator("//span[text()='Products']")).to_be_visible()
        p3 = page.locator("//div[@class='inventory_item']").count()

        page.locator("//button[normalize-space()='Open Menu']").click()
        page.locator("//a[normalize-space()='Logout']").click()

# Cách 4:
        page.locator("[data-test='username']").fill("performance_glitch_user")
        page.locator("[data-test='password']").fill("secret_sauce")

        page.locator("[data-test='login-button']").click()

        expect(page.locator("//span[contains(@class, 'title')]")).to_be_visible()
        p4 = page.locator("//div[contains(@class, 'inventory_item')]")

        page.locator("//button[normalize-space()='Open Menu']").click()
        page.locator("//a[normalize-space()='Logout']").click()

# Cách 5:
        page.locator("//input[contains(@placeholder, 'Username')]").fill("visual_user")
        page.locator("//input[contains(@placeholder, 'Password')]").fill("secret_sauce")

        page.locator("//input[contains(@value, 'Login')]").click()

        expect(page.locator("//span[contains(@class, 'title')]")).to_be_visible()
        p5 = page.locator("//div[contains(@class, 'inventory_item')]").count()

        products = [p1, p3, p4, p5]
        print(f" Số lượng sản phẩm đang hiển thị trên trang: {products}")

def test_web_login_failed(page : Page):
        page.goto("https://www.saucedemo.com/")

        page.get_by_placeholder("Username").fill("standard_user")
        page.get_by_placeholder("Password").fill("abc")

        page.get_by_role("button", name="Login").click()

        error_message = page.locator("[data-test='error']")
        expect(error_message).to_contain_text("Username and password do not match")

        print("Thông báo lỗi hiển thị chính xác.")
