from playwright.sync_api import Page, expect
import re, time

def test_delete_project(page: Page):
        # Test URL
        TEST_URL = "https://hrm.anhtester.com/erp/login"

        # Login credentials
        username = "admin_example"
        password = "123456"

         # Project information
        projectTitle = "Test project 321"
        client = "WOF Wind 2303"
        projectSummary = "This is the project summary"

        # Open URL
        page.goto(TEST_URL)

        # Login
        page.locator('//input[@id="iusername"]').fill(username)
        page.locator('//input[@id="ipassword"]').fill(password)
        page.locator('//button[@type="submit" or normalize-space()="Login"]').click()

        # Check username display
        username_label = page.locator('//a[contains(@href,"my-profile")]//p')
        expect(username_label).to_contain_text('@admin_example')

        # Click Projects menu item
        page.locator('//div[@class="navbar-wrapper"]//li//a[contains(@href,"projects-list")]').click()

        # Search newly created project
        page.locator('//div[@id="xin_table_wrapper"]//input[@type="search"]').fill(projectTitle)

        # Hover at the row of created project to display Delete button
        page.locator('//table[@id="xin_table"]//tbody//tr[1]').hover()
        time.sleep(3)

        # Click View Details button
        page.locator('//a[contains(@href,"project-detail")]//button[@type="button"]').click()
        time.sleep(3)

        # Switch to Edit tab
        page.locator('//div[@class="card-body"]//li//a[@id="pills-edit-tab"]').click()
        time.sleep(3)

        # Change title
        page.locator('//input[@name="title" or @placeholder="title"]').fill('Test project 111')
        time.sleep(3)

        # Click Upload Project button
        page.locator('//button[@type="submit"]//span[normalize-space()="Update Project"]').click()
        time.sleep(3)

        # Go back Projects page
        page.locator('//div[@class="navbar-wrapper"]//li//a[contains(@href,"projects-list")]').click()
        time.sleep(3)

        # Search the project which title was changed...
        search_field = page.locator('//div[@id="xin_table_wrapper"]//input[@type="search"]').fill(projectTitle)
        time.sleep(5)

        # Check the result row contains the valid message
        result_row = page.locator('//table[@id="xin_table"]/tbody/tr[1]')
        expect(result_row).to_contain_text('No records available')

        time.sleep(3)




        