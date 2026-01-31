from datetime import datetime
from playwright.sync_api import Page, expect

def createDateTimeString():
    currentTime = datetime.now()
    stringDateTime = currentTime.strftime("%Y-%m-%d %H:%M")

    result = 'TUNGNS ' + stringDateTime
    return result

def test_erp_locator(page : Page):
    page.goto("https://hrm.anhtester.com")

    page.locator("//input[@name='iusername']").fill("admin_example")
    page.locator("//input[@name='password']").fill("123456")

    page.locator("//button[@type='submit']").click()

    # MENU SIDEBAR
    page.locator("//div[@class='navbar-wrapper']//a[normalize-space()='Core HR']").click()
    page.locator("//div[@class='navbar-wrapper']//a[normalize-space()='Department']").click()

    # Create data input
    name = createDateTimeString()

    # Input name
    page.locator("//div[@class='form-group']//input[@type='text']").fill(name)
    # Click button Save
    page.locator("//div[@class='card']//button").click()
    # Input name
    page.locator("//input[@type='search']").fill(name)

    # Assertion add successfully
    expect(page.locator("//tbody//tr[1]//td[@class='sorting_1']")).to_contain_text(name)

    # Wait for popup add successfully disappear
    page.wait_for_timeout(5000)

    # Click button Delete
    page.locator("//table//span[@data-original-title='Delete']").click()
    # Click button Submit
    page.locator("//div[@class='modal-content']//button[@type='submit']").click()

    # Assertion delete successfully
    expect(page.locator("//div[@class='toast-message']")).to_contain_text('Department deleted.')

