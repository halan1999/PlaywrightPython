from playwright.sync_api import Page, expect
import time

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

    # Add New Department
    departmentName = 'Thanh Ngân'
    page.locator("//input[@placeholder='Name']").fill(departmentName)
    page.locator("//span[normalize-space()='Save']").click()
    # Search the the new added department
    time.sleep(2)
    page.locator("//input[@type='search']").fill(departmentName)
    time.sleep(2)
    results = page.locator("//table//tbody//tr").count()
    if results > 0:
        expect(page.locator("//table//tbody//tr[1]//td[1]")).to_have_text(departmentName)
        print("Đã tìm thấy kết quả tìm kiếm")
    else:
        print("Không tìm thấy kết quả tìm kiếm")
