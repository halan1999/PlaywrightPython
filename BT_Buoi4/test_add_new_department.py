from playwright.sync_api import Page, sync_playwright, expect
import re, time

def test_add_new_department(page: Page):
# go to hrm page then login
    page.goto("https://hrm.anhtester.com/")
    page.get_by_placeholder("Your Username").fill("admin_example")
    page.get_by_placeholder("Enter Password").fill("123456")
    page.get_by_role("button", name="Login").click()
# find and go to the department page
    page.locator("//a[@class='pc-link sidenav-toggle' and normalize-space()='Core HR']").click()
    page.locator("//a[normalize-space()='Department']").click()
# add new department
    page.get_by_placeholder('Name').fill('hanh-nguyen')
    page.get_by_role("button", name = "Save").click()
# search and click edit department
    page.get_by_label("Search").fill("hanh-nguyen")
    page.locator("(//td[@class='sorting_1'])[1]").hover()
    page.locator("(//i[@class='feather icon-edit'])[1]").click()
# update name in popup   
    page.locator("//div[@class='modal-body']//input").fill("hanh-nguyen-edit-ne")
    page.get_by_role("button", name = "Update").click()
# search and click delete department
    page.get_by_label("Search").fill("hanh-nguyen-5")
    page.locator("(//td[@class='sorting_1'])[1]").hover()
    page.locator("(//i[@class='feather icon-trash-2'])[1]").click()
# delete department in popup
    page.get_by_role("button", name = "Confirm").click()
    
    time.sleep(5)