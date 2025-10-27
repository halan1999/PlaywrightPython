from playwright.sync_api import Page, expect
from utils.project_information_storage import load_project_title
import re, time, random, string

def generate_random_id(length=6):
    characters = string.ascii_uppercase + string.digits  # A-Z + 0-9
    return ''.join(random.choice(characters) for _ in range(length))

def test_delete_project(page: Page):
        # Test URL
        TEST_URL = "https://hrm.anhtester.com/erp/login"

        # Login credentials
        username = "admin_example"
        password = "123456"

         # Project information
        projectTitle = load_project_title()

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
        page.locator('//a[normalize-space(.)="Projects"]').click()

        # Search newly created project
        page.locator('//div[@id="xin_table_wrapper"]//input[@type="search"]').fill(projectTitle)

        # Hover at the row of created project to display Delete button
        page.locator('//table[@id="xin_table"]//tbody//tr[1]').hover()
        time.sleep(3)

        # Click Delete button
        page.locator('//button[@data-target=".delete-modal"]').click()
        time.sleep(3)

        # Modal opens...
        expect(page.locator('//div[@class="modal-content"]//h5[contains(normalize-space(),"delete")]')).to_contain_text('Are you sure you want to delete this record?')
        expect(page.locator('//div[@class="alert alert-danger"]/strong')).to_contain_text("You won't be able to revert this!")

        # Click Confirm button
        page.locator('//div[@class="modal-content"]//button[normalize-space()="Confirm"]').click()

        # Search the project which was deleted...
        page.locator('//div[@id="xin_table_wrapper"]//input[@type="search"]').fill(projectTitle)
        time.sleep(3)

        # Check the result row contains the valid message
        result_row = page.locator('//table[@id="xin_table"]/tbody/tr[1]')
        expect(result_row).to_contain_text('No records available')

        time.sleep(3)




        