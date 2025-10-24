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

    # Assertion
    expect(page.locator("//tbody//tr[1]//td[@class='sorting_1']")).to_contain_text(name)


