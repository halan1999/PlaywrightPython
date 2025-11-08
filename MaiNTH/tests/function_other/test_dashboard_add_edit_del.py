import re
from playwright.sync_api import Playwright, sync_playwright, expect


def test_dashboard_add_edit_del_flow(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    # Go to https://hrm.anhtester.com/erp/login
    page.goto("https://hrm.anhtester.com/erp/login")
    page.get_by_role("textbox", name="Your Username").click()
    page.get_by_role("textbox", name="Your Username").fill("admin_example")
    page.get_by_role("textbox", name="Enter Password").click()
    page.get_by_role("textbox", name="Enter Password").fill("123456")
    page.get_by_role("button", name=" Login").click()
    print("Login successfully")
    # Navigate to Department module
    page.get_by_role("link", name="Core HR").click()
    page.get_by_role("link", name="Department").click()
    # Add Departments
    page.get_by_role("textbox", name="Name").click()
    page.get_by_role("textbox", name="Name").fill("MaiNTH_test_1")
    page.get_by_role("button", name="Save").click()
    page.get_by_role("textbox", name="Name").click()
    page.get_by_role("textbox", name="Name").fill("MaiNTH_test_2")
    page.get_by_role("button", name="Save").click()
    print("Added Departments successfully")
    # Search and Update Department
    page.get_by_role("searchbox", name="Search").click()
    page.get_by_role("searchbox", name="Search").fill("MaiNTH_test_1")
    print
    # Edit Department
    page.get_by_role("button", name="").click()
    page.locator("#edit_department").get_by_role("textbox", name="Name").click()
    page.locator("#edit_department").get_by_role("textbox", name="Name").fill("MaiNTH_test_1_update")
    page.get_by_role("button", name="Update").click()
    print
    # Search updated Department
    page.get_by_role("searchbox", name="Search").click()
    page.get_by_role("searchbox", name="Search").fill("MaiNTH_test_1_update")
    print
    # Delete Departments
    page.get_by_role("button", name="").click()
    page.get_by_role("button", name="Confirm").click()
    print("Deleted Department 1 successfully")

    # ---------------------
    context.close()
    browser.close()


# with sync_playwright() as playwright:
#     run(playwright)
