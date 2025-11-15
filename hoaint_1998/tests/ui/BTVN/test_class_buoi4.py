from playwright.sync_api import Page, expect
from faker import Faker

url: str = "https://hrm.anhtester.com/erp/login"

def test_btvn_actions_and_assertions(page: Page):
    faker = Faker()
    # login
    page.goto(url)
    page.locator("//input[@id='iusername']").fill("admin_example")
    page.locator("//input[@id='ipassword']").fill("123456")
    page.locator("//button[@type='submit']").click()

    #verify login success
    expect(page).to_have_url("https://hrm.anhtester.com/erp/desk")

    # transition to [Core HR].[Department]
    page.locator("//a[normalize-space()='Core HR']").click()
    page.locator("//a[normalize-space()='Department']").click()

    # add new department
    name = faker.name_female()
    page.locator("//input[@name='department_name']").fill(name)
    page.locator("//span[normalize-space()='Save']").click()
    #verify add new success
    expect(page.locator("//div[@id='toast-container']")).to_contain_text("Department added")

    # perform search
    search_input = page.locator("//input[@type='search']")
    # enter keywork
    search_input.fill(name)
    search_input.press("Enter")
    # check result 
    row1_cell1_locator = page.locator(f"//tbody//tr[1]/td[normalize-space()='{name}']")
    expect(row1_cell1_locator).to_have_text(name)

    # perform edit
    # click button edit of record
    page.locator(f"//table//tr[td[normalize-space()='{name}']][1]//span[1]").click()
    #verify popup edit
    popup_edit = page.locator("//form[@id='edit_department']")
    expect(popup_edit).to_be_visible()
    # edit department
    edit_name = faker.name_female()
    page.locator("//div[@class='modal-body']//input[@name='department_name']").fill(edit_name)
    page.locator("//span[normalize-space()='Update']").click()
    #verify edit new success
    expect(page.locator("//div[@id='toast-container']")).to_contain_text("Department updated")

    #search the old name department
    # perform search
    search_input = page.locator("//input[@type='search']")
    # enter keywork
    search_input.fill(name)
    search_input.press("Enter")
    # check result 
    number_row = page.locator("//tbody//tr").count()
    print(f"NUMBER ROW = {number_row}")

    expect(page.locator("//tbody//tr[1]/td[1]")).not_to_have_text(name)

    #perform delete
    # enter keywork
    search_input.fill(edit_name)
    search_input.press("Enter")
    # check result 
    row1_cell1_locator = page.locator(f"//tbody//tr[1]/td[normalize-space()='{edit_name}']")
    expect(row1_cell1_locator).to_have_text(edit_name)
    #click button delete
    page.locator(f"//table//tr[td[normalize-space()='{edit_name}']][1]//span[2]").click()
    #verify popup delete
    popup_delete = page.locator("//form[@id='delete_record']")
    expect(popup_delete).to_be_visible()
    page.locator("//span[normalize-space()='Confirm']").click()
    #verify delete success
    expect(page.locator("//div[@id='toast-container']")).to_contain_text("Department deleted")
    #check record in lisst
    # enter keywork
    search_input.fill(edit_name)
    search_input.press("Enter")
    expect(page.locator("//tbody//tr[1]/td[1]")).not_to_have_text(edit_name)

    
