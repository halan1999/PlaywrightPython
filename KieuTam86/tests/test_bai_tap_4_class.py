from playwright.sync_api import Page, expect, Playwright
import re, time

def test_login(page: Page):
    url = "https://hrm.anhtester.com/erp/login"
    page.goto(url)
    page.locator("#iusername").fill("admin_example")
    page.locator("#ipassword").fill("123456")
    login_button = page.get_by_role("button", name="Login").click()
    print("✅ Đăng nhập thành công!")

def test_define_elements_(page: Page):
    expect(page.get_by_text("Your Apps")).to_be_visible()
    expect(page).to_have_url("https://hrm.anhtester.com/erp/desk#")

    #choose Core HR
    page.locator("//a[@class='pc-link sidenav-toggle' and normalize-space()='Core HR']").click()
    #choose Department
    page.locator("//a[@class='pc-link' and normalize-space()='Department']").click()

    expect(page.get_by_text("List All Departments")).to_be_visible()

    #Determine sub menu
    page.locator("//div[@class='text-muted small' and normalize-space()='Set up Departments']").click()

    # Add new department
    new_dep = "tam new department"
    page.locator("//input[@name='department_name' and @placeholder='Name']").fill(new_dep)
    page.locator("//button[.//span[normalize-space()='Save']]").click()

    # Search new department
    page.locator("//input[@type='search']").fill(new_dep)

    #Check new department
        #Determine table
    page.locator("//table[@id='xin_table']")

    




