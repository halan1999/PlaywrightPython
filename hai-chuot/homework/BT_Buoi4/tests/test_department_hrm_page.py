from playwright.sync_api import Page, expect
import time

# NOTE: Execute Test case 
def test_corehr_department(page : Page):
    BASE_URL = 'https://hrm.anhtester.com/erp/login'
    USER_ADMIN = 'admin_example'
    PASSWORD_ADMIN = '123456'
    PREFIX_INPUT_DATA_NAME = 'haichuot'

     # Navigate link test 
    page.goto(BASE_URL)

    # Input username
    page.locator('//input[@id="iusername"]').fill(USER_ADMIN)

    # Input password
    page.locator('//input[@id="ipassword"]').fill(PASSWORD_ADMIN)

    # Click Buttton Login
    page.locator('//button[@type="submit"]').click()

    # Verify username
    label_username = page.locator('//a[@href="https://hrm.anhtester.com/erp/my-profile"]//p')
    expect(label_username).to_contain_text(USER_ADMIN)

     # Click Menu Core HR
    page.locator('//a[normalize-space()="Core HR"]').click()

    # Click Sub Menu Department
    page.locator('//a[normalize-space()="Core HR"]/following-sibling::ul//a[normalize-space()="Department"]').click()

     # Click Tab Department
    page.locator('//ul[contains(@class,"nav-tabs")]//a[@href="https://hrm.anhtester.com/erp/departments-list"]').click()
    
    # Fill textbox Name    
    input_data_name = create_input_data_name(page, PREFIX_INPUT_DATA_NAME)
    page.locator('//input[@name="department_name"]').fill(input_data_name)

    # Button Save
    page.locator('//span[normalize-space()="Save"]/parent::button').click()

    time.sleep(2)

    # NOTE: Compare actual results with expected results
    # Fill textbox Search prefix
    page.locator('//input[@type="search" and @aria-controls="xin_table"]').fill(input_data_name)

    time.sleep(2)

    # Verify actual result
    assert_result(page, input_data_name)
    
# NOTE: Function for Test case
def assert_result(page : Page, expected_result : str):
    # Get all inner text in column "Department Name" for each row
    actual_value = page.locator('//table[@id="xin_table"]/tbody//td[1]').inner_text()
    
    assert actual_value == expected_result

def create_input_data_name(page : Page, prefix : str):
    timestamp = int(time.time() * 1000)
    return f"{prefix}{timestamp}"