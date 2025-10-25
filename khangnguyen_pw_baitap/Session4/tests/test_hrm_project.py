from playwright.sync_api import Page, expect
import re, time
import random

def test_hrm_project(page: Page):
        # Test URL
        TEST_URL = "https://hrm.anhtester.com/erp/login"

        # Login credentials
        username = "admin_example"
        password = "123456"

         # Project information
        projectTitle = "Test project 123"
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
        menu_item_core_hr = page.locator('//a[normalize-space(.)="Projects"]').click()

        # Click Add new button
        add_new_button = page.locator('//a[@href="#add_form" and contains(normalize-space(.), "Add New")]').click()

        # Input project title
        title_field = page.locator('//input[@name="title" and @type="text"]').fill(projectTitle)
        # Input client
        client_field = page.locator('//span[@data-select2-id="83"]').click()
        select_option = page.locator('//li[@role="option" and normalize-space()="WOF Wind 2303"]').click()
        # Input start date
        page.locator('//input[@name="start_date"]').click()
        page.locator("div.dtp:visible .dtp-select-day", has_text="27").click()
        page.locator("div.dtp:visible button.dtp-btn-ok").click()
        # Input end date
        page.locator('//input[@name="end_date"]').click()
        page.locator("div.dtp:visible .dtp-select-day", has_text="31").click()
        page.locator("div.dtp:visible button.dtp-btn-ok").click()

        # Input summary
        page.locator('//textarea[@id="summary"]').fill(projectSummary)

        # Click Save
        page.locator('//div[@class="card-footer text-right"]//button[@type="submit"]').click()

        time.sleep(2)

        # Search newly created project
        search_field = page.locator('//div[@id="xin_table_wrapper"]//input[@type="search"]').fill(projectTitle)
        time.sleep(5)

        # Check project title displayed at the first cell of Projects column
        project_title_cell = page.locator('//table//tbody/tr[@role="row"][1]/td[1]')
        client_cell = page.locator('//table//tbody/tr[@role="row"][1]/td[2]')
        expect(project_title_cell).to_contain_text(projectTitle)
        expect(client_cell).to_contain_text(client)





        