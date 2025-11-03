from playwright.sync_api import Page, expect

def test_saucedemo_page(page : Page):
    url_test = "https://www.saucedemo.com/"
    
    page.goto(url_test)

    page.get_by_placeholder("Username").fill('standard_user')
    page.get_by_placeholder("Password").fill('secret_sauce')

    page.get_by_role("button", name="Login").click()

    expect(page.get_by_text("Products")).to_be_visible()

    list_products = page.locator('//div[@class="inventory_item"]')

    print(f'Tổng số lượng sản phẩm là: {list_products.count}')
