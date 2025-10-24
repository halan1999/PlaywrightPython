from playwright.sync_api import Page, expect
import re, time

def test_login(page: Page):
    #access https://hrm.anhtester.com/erp/login
    page.goto("https://hrm.anhtester.com/erp/login")
    #input username and password
    page.get_by_placeholder("Your Username").click()
    page.get_by_placeholder("Your Username").fill("admin_example")
    page.get_by_placeholder("Enter Password").click()
    page.get_by_placeholder("Enter Password").fill("123456")
    page.locator("//button[@type='submit']").click()
    page.goto("https://hrm.anhtester.com/erp/desk")
    #click on CoreHR to open menu
    page.locator("(//li[contains(@class, 'pc-item')]//a[contains(@class, 'pc-link') and contains(@class, 'sidenav-toggle')])[2]").click()
    page.locator("//a[@class='pc-link' and normalize-space()='Department']").click()
    page.locator("https://hrm.anhtester.com/erp/departments-list") 
    #Add new department
    page.get_by_placeholder("name").click()
    page.get_by_placeholder("name").fill("tri department 02")
    page.locator("(//button[@type='submit'])[1]").click()
    # check the new value on table by search function
    page.locator("//input[@type='search']").click()
    page.locator("//input[@type='search']").fill("tri department 02")
    page.wait_for_selector("#xin_table")
    table = page.locator("#xin_table")
    expect(table).to_contain_text("tri department 02")
    time.sleep(5)