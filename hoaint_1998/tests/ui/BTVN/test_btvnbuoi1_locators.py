from playwright.sync_api import Page, expect

url: str = "https://www.saucedemo.com"

def test_locators_css_id(page: Page):
    
    page.goto(url)

    username_input = page.locator("#user-name")
    password_input = page.locator("#password")
    login_button = page.locator("#login-button")
    logo_element = page.get_by_text("Products")

    username_input.fill("standard_user")
    password_input.fill("secret_sauce")
    login_button.click()
    expect(page).to_have_url(f"{url}/inventory.html")
    expect(logo_element).to_be_visible()
    list_items = page.locator(".inventory_item")
    print(f"Số lượng sản phẩm hiển thị: {list_items.count()}")


def test_locators_xpath_id(page: Page):
    
    page.goto(url)

    username_input = page.locator('//*[@id="user-name"]')
    password_input = page.locator('//*[@id="password"]')
    login_button = page.locator('//*[@id="login-button"]')
    error_message = page.locator('//*[@data-test="error"]')

    username_input.fill("locked_out_user")
    password_input.fill("secret_sauce")
    login_button.click()
    expect(error_message).to_be_visible()

def test_locators_playwright(page: Page):
    
    page.goto(url)

    username_input = page.get_by_placeholder("Username")
    password_input = page.get_by_placeholder("Password")
    login_button = page.get_by_role("button", name="Login")

    username_input.fill("problem_user")
    password_input.fill("secret_sauce")
    login_button.click()
    expect(page).to_have_url(f"{url}/inventory.html")
    list_items = page.locator("//div[@data-test='inventory-item']")
    print(f"Số lượng sản phẩm hiển thị: {list_items.count()}")

def test_locators_css_attribute(page: Page):
    
    page.goto(url)

    username_input = page.locator('input[data-test="username"]')
    password_input = page.locator('input[data-test="password"]')
    login_button = page.locator('input[data-test="login-button"]')

    username_input.fill("performance_glitch_user")
    password_input.fill("secret_sauce")
    login_button.click()
    expect(page).to_have_url(f"{url}/inventory.html")
    list_items = page.locator("//div[@data-test='inventory-item']")
    print(f"Số lượng sản phẩm hiển thị: {list_items.count()}")

def test_locators_xpath_attribute(page: Page):
    
    page.goto(url)

    username_input = page.locator('//input[@data-test="username"]')
    password_input = page.locator('//input[@data-test="password"]')
    login_button = page.locator('//input[@data-test="login-button"]')

    username_input.fill("error_user")
    password_input.fill("secret_sauce")
    login_button.click()
    expect(page).to_have_url(f"{url}/inventory.html")
    list_items = page.locator("//div[@data-test='inventory-item']")
    print(f"Số lượng sản phẩm hiển thị: {list_items.count()}")

def test_locators_xpath_type(page: Page):
    
    page.goto(url)

    username_input = page.locator('//input[@type="text"]')
    password_input = page.locator('//input[@type="password"]')
    login_button = page.locator('//input[@type="submit"]')

    username_input.fill("visual_user")
    password_input.fill("secret_sauce")
    login_button.click()
    expect(page).to_have_url(f"{url}/inventory.html")
    list_items = page.locator("//div[@data-test='inventory-item']")
    print(f"Số lượng sản phẩm hiển thị: {list_items.count()}")
