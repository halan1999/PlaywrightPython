from playwright.sync_api import  Page, expect
import re, time
#locator
# def test_hrmanhtester (page: Page):
#     page.goto('https://hrm.anhtester.com/erp/login')
#     page.locator("//input[@id='iusername']").fill("admin_example")
#     page.locator("//input[@id='ipassword']").fill("123456")
#     page.locator("//button[@type='submit']").click()
#     page.locator("//li//a[normalize-space(.)='Core HR']").click()
#     page.locator("//a[normalize-space(.)='Department']").click()
#     page.locator("//input[@name='department_name' and @type='text']").fill("Ducnt")
#     page.locator("//span[normalize-space(.)='Save']").click()
#     expect(page.locator("//td[contains(normalize-space(.),'ducnt')]")).to_be_visible()

#     time.sleep(5)
#dropdown kiem tra trang thai the chuyen sang true khi bam vao dropdown
def test_hrmdropdown (page : Page):
    page.goto('https://crm.anhtester.com/authentication/login')
    page.locator("//input[@id='iusername']").fill("admin_example")
    page.locator("//input[@id='ipassword']").fill("123456")
    page.locator("//button[@type='submit']").click()
    time.sleep(3)