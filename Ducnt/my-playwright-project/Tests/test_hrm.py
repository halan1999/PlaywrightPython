from playwright.sync_api import  Page, expect
import re, time
import pytest
#locator
@pytest.fixture(scope='function')
def login_hrmanhtester(page: Page):
    page.goto('https://hrm.anhtester.com/erp/login')
    page.locator("//input[@id='iusername']").fill("admin_example")
    page.locator("//input[@id='ipassword']").fill("123456")
    page.locator("//button[@type='submit']").click()
    page.wait_for_load_state("networkidle")
    yield page
def test_baihrm(login_hrmanhtester: Page):
    page = login_hrmanhtester
    page.locator("//li//a[normalize-space(.)='Core HR']").click()
    page.locator("//a[normalize-space(.)='Department']").click()
    page.locator("//input[@name='department_name' and @type='text']").fill("Ducnt")
    page.locator("//span[normalize-space(.)='Save']").click()
    page.wait_for_load_state("networkidle")
    page.wait_for_selector("//td[contains(normalize-space(.),'Ducnt')]")
    expect(page.locator("//td[contains(normalize-space(.),'Ducnt')]").first).to_be_visible()
    page.locator("//input[@type='search']").fill("Ducnt")
    page.locator("//input[@type='search']").press("Enter")
    page.wait_for_load_state("networkidle")
    expect(page.locator("//td[normalize-space(.)='Ducnt']").first).to_be_visible()
  

    time.sleep(5)
