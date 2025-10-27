from playwright.sync_api import Page,expect
import time,re,pytest
@pytest.fixture
def login(page:Page):
    page.goto("https://hrm.anhtester.com/erp/login")
    page.locator("//input[@id='iusername']").fill("admin_example")
    page.locator("//input[@id='ipassword']").fill("123456")
    page.locator("//span[@class='ladda-label']").click()
    expect(page.get_by_text("Welcome admin_example hello")).to_be_visible()

@pytest.mark.usefixtures("login")
def test_add_department(page:Page):   
    page.locator("//a[normalize-space()='Core HR']").click()
    page.locator("//a[normalize-space()='Department']").click()

    # Add Name
    name = page.locator("//input[@placeholder='Name']")
    name.fill("thanh1")
    expect (name).to_have_value("thanh1")
    page.locator("//div[@class='card-footer text-right']//button[@type='submit']").click()
    toast_message = page.locator("//div[@class='toast-message']")
    expect (toast_message).to_contain_text("Department added.")
    page.wait_for_selector("//div[@class='toast-message']", state="detached", timeout=10000)
    #Search
    search = page.locator("//input[@type='search']")
    search.fill("thanh1")
    expect (search).to_have_value("thanh1")
    result = page.locator("(//tr[@role='row']//td[@class='sorting_1'])[1]")
    expect (result).to_contain_text("thanh1")
    