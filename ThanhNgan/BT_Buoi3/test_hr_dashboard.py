from playwright.sync_api import Page

def test_erp_dashboard(page: Page):
    # Navigate to https://hrm.anhtester.com/
    print("\nNavigate to the web")
    page.goto("https://hrm.anhtester.com/erp/login")

    # Login
    page.locator("#iusername").fill("admin_example")
    page.locator("#ipassword").fill("123456")
    page.locator("//span[contains(text(),'Login')]").click()
    print("Login successfully")

    # NOTE: Core HR
    print("\nNavigate to the Core HR>Department")
    # page.locator("//div[@class='hamburger-box']").click()
    page.locator("//a[normalize-space()='Core HR']").click()
    page.locator("//a[normalize-space()='Department']").click()

    # Zone: Department
    page.locator("//div[@id='smartwizard-2']//a[contains(@href, '/designation-list')]").click()
    page.locator("//div[@id='smartwizard-2']//a[contains(@href, '/news-list')]").click()
    page.locator("//div[@id='smartwizard-2']//a[contains(@href, '/policies-list')]").click()
    page.locator("//div[@id='smartwizard-2']//a[contains(@href, '/departments-list')]").click()



    # Tab: Department
    page.locator("//input[@name='department_name']").fill("Thanh Ngân")
    page.locator("//span[normalize-space()='Save']").click()
