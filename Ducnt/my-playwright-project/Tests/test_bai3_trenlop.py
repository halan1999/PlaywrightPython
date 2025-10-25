from playwright.sync_api import  Page, expect
import re, time

def test_crmanhtester (page: Page):
    page.goto('https://crm.anhtester.com/admin')
    page.locator("//div//input[@id='email']").fill("admin@example.com")
    page.locator("//div//input[@id='password']").fill("123456")
    page.click("//button[@type='submit']")
    page.locator("//span[contains(normalize-space(.),'Dashboard')]").click()
    page.locator("//input[contains(@id,'search_input')]").fill("ducnt")
    expect(page.locator("//li[contains(@class,'padding-5 text-center search-no-results')]")).to_be_visible()
    time.sleep(5)

   