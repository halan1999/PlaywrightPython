from playwright.sync_api import Page, expect
import re, time
import random

def test_project_table_columns(page: Page):
        # Test URL
        TEST_URL = "https://hrm.anhtester.com/erp/login"

        # Login credentials
        username = "admin_example"
        password = "123456"

        # Open URL
        page.goto(TEST_URL)

        # Table headings
        projects_table_heading = page.locator('//table[@id="xin_table"]//tr//th[1]')
        client_table_heading = page.locator('//table[@id="xin_table"]//tr//th[2]')
        started_date_table_heading = page.locator('//table[@id="xin_table"]//tr//th[3]')
        ended_date_table_heading = page.locator('//table[@id="xin_table"]//tr//th[4]')
        team_table_heading = page.locator('//table[@id="xin_table"]//tr//th[5]')
        priority_table_heading = page.locator('//table[@id="xin_table"]//tr//th[6]')
        progress_table_heading = page.locator('//table[@id="xin_table"]//tr//th[7]')

        # Login
        page.locator('//input[@id="iusername"]').fill(username)
        page.locator('//input[@id="ipassword"]').fill(password)
        page.locator('//button[@type="submit" or normalize-space()="Login"]').click()

        # Check username display
        username_label = page.locator('//a[contains(@href,"my-profile")]//p')
        expect(username_label).to_contain_text('@admin_example')
        time.sleep(5)

        # Click Projects menu item
        page.locator('//a[normalize-space(.)="Projects"]').click()
        time.sleep(5)

        # Check table headings are displayed correctly
        expect(projects_table_heading).to_contain_text('Projects')
        expect(client_table_heading).to_contain_text('Client')
        expect(started_date_table_heading).to_contain_text('Start Date')
        expect(ended_date_table_heading).to_contain_text('End Date')
        expect(team_table_heading).to_contain_text('Team')
        expect(priority_table_heading).to_contain_text('Priority')
        expect(progress_table_heading).to_contain_text('Process')