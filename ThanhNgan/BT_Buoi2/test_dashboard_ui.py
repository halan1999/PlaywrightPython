from playwright.sync_api import Page, expect, playwright
import re

def test_dashboard_element(page: Page):
    page.goto("https://crm.anhtester.com/admin")

    page.locator('#email').fill("admin@example.com")
    page.locator('#password').fill("123456")

    page.get_by_role('button',name='Login').click()
    expect(page).to_have_url(re.compile("https://crm.anhtester.com/admin"))

    # NOTE: Khu vực Menu
    # icon Dashboard
    print("\nFind Menu Dashboard elements...")

    page.locator("//span[contains(text(),'Dashboard')]")
    # icon Customers
    page.locator("//span[contains(text(),'Customers')]")
    # icon Sales
    page.locator("//span[contains(text(),'Sales')]")
    # icon Subscriptions
    page.locator("//span[contains(text(),'Subscriptions')]")
    # icon Expenses
    page.locator("//span[contains(text(),'Expenses')]")
    # icon Contracts
    page.locator("//span[contains(text(),'Contracts')]")
    # icon Projects
    page.locator("//span[contains(text(),'Projects')]")
    # icon Tasks
    page.locator("//span[contains(text(),'Tasks')]")
    # icon Support
    page.locator("//span[contains(text(),'Support')]")
    # icon Leads
    page.locator("//span[contains(text(),'Leads')]")
    # icon Estimate Request
    page.locator("//span[contains(text(),'Estimate Request')]")
    # icon Knowledge Base
    page.locator("//span[contains(text(),'Knowledge Base')]")
    # icon Utilities
    page.locator("//span[contains(text(),'Utilities')]")
    # icon Reports
    page.locator("//span[contains(text(),'Reports')]")
    
    print("Find all menu elements successfully")