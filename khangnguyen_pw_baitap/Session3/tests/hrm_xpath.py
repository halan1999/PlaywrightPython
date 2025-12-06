from playwright.sync_api import Page, expect
import re, time

def test_xpath_locating(page: Page):
     page.goto("https://hrm.anhtester.com/erp/login")

     # Login form
     username_field = page.locator('//input[@id="iusername"]')
     password_field = page.locator('//input[@id="ipassword"]')
     login_button = page.locator('//button[@type="submit" or normalize-space()="Login"]')


     username_field.fill('admin_example')
     password_field.fill('123456')
     login_button.click()

     time.sleep(5)

     # Menu Items
     menu_item_core_hr = page.locator('//a[normalize-space(.)="Core HR"]').click()
     sub_menu_item_department = page.locator('//a[normalize-space()="Department"]').click()

     time.sleep(5)

     # Page header
     page_header_home = page.locator('//div[@class="page-header"]/descendant::a[normalize-space()="Home"]')

     # Page navigation
     page_navigation_department = page.locator('//div[@id="smartwizard-2"]/descendant::a[contains(@href,"/departments-list")]')
     page_navigation_designation = page.locator('//div[@id="smartwizard-2"]/descendant::a[contains(@href,"/designation-list")]')
     page_navigation_annoucements = page.locator('//div[@id="smartwizard-2"]/descendant::a[contains(@href,"/news-list")]')
     page_navigation_policies = page.locator('//div[@id="smartwizard-2"]/descendant::a[contains(@href,"/policies-list")]')

     # Add New Department
     field_department_name = page.locator('//input[@name="department_name"]').fill('Khang Department Ahihi')
     save_button = page.locator('//button[@type="submit"]/child::span[normalize-space()="Save"]').click()

     time.sleep(5)

     # List Deparments
     search_field = page.locator('//div[@id="xin_table_filter"]/descendant::input[@type="search"]').fill('Khang Department')
     field_dropdown_entries = page.locator('//select[@name="xin_table_length"]')

     time.sleep(5)

     first_row = page.locator('//table[@id="xin_table"]/descendant::tr[1]')
     department_name__first_row = page.locator('//table[@id="xin_table"]/descendant::tr[2]/child::td[1]')

     expect(first_row).to_be_visible()
     expect(department_name__first_row).to_contain_text('Khang')

     time.sleep(10)








