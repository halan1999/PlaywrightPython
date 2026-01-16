import re
from playwright.sync_api import Page, expect


def test_element_menu(page: Page):
    
    # Goto page
    page.goto("https://crm.anhtester.com/admin/authentication")
    # Login
    page.get_by_role("textbox", name="Email Address").fill("admin@example.com")
    page.get_by_role("textbox", name="Password").fill("123456")
    page.get_by_role("button", name="Login").click()
    #  Locator Menu
    #  Click menu Dashboard
    page.locator("//span[@class='menu-text'][normalize-space()='Dashboard']").click()
    #  Click menu Customers
    page.locator("//span[@class='menu-text'][normalize-space()='Customers']").click()


    # Click menu Sales 
    page.locator("//span[@class='menu-text'][normalize-space()='Sales']").dblclick()
    print("Clicked on Sales menu")
    # wait for 2 seconds
    page.wait_for_timeout(2000)
    # Click menu Proposals
    page.locator("//span[@class='sub-menu-text'][normalize-space()='Proposals']").click()
    # Click menu Estimates
    page.locator("//span[@class='sub-menu-text'][normalize-space()='Estimates']").click()
    # Click menu Invoices
    page.locator("//span[@class='sub-menu-text'][normalize-space()='Invoices']").click()
    # Click menu Payments
    page.locator("//span[@class='sub-menu-text'][normalize-space()='Payments']").click()
    # Click menu Credit Notes
    page.locator("//span[@class='sub-menu-text'][normalize-space()='Credit Notes']").click()
    # Click menu Items 
    page.locator("//span[@class='sub-menu-text'][normalize-space()='Items']").click()


    # Click menu Subscriptions
    page.locator("//span[@class='menu-text'][normalize-space()='Subscriptions']").click()
    # Click menu Expenses
    page.locator("//span[@class='menu-text'][normalize-space()='Expenses']").click()
    # Click menu Contracts
    page.locator("//span[@class='menu-text'][normalize-space()='Contracts']").click()
    # Click menu Projects
    page.locator("//span[@class='menu-text'][normalize-space()='Projects']").click()
    # Click menu Tasks
    page.locator("//span[@class='menu-text'][normalize-space()='Tasks']").click()
    # Click menu Support
    page.locator("//span[@class='menu-text'][normalize-space()='Support']").click()
    # Click menu Leads
    page.locator("//span[@class='menu-text'][normalize-space()='Leads']").click()
    # Click menu Estimate Request
    page.locator("//span[@class='menu-text'][normalize-space()='Estimate Request']").click()
    # Click menu Knowledge Base
    page.locator("//span[@class='menu-text'][normalize-space()='Knowledge Base']").click()


    # Click menu Utilities
    page.locator("//span[@class='menu-text'][normalize-space()='Utilities']").click()
    # Click menu Media
    page.locator("//span[@class='sub-menu-text'][normalize-space()='Media']").click()
    # Click menu Bulk PDF Export
    page.locator("//span[@class='sub-menu-text'][normalize-space()='Bulk PDF Export']").click()
    # Click menu Calendar
    page.locator("//span[@class='sub-menu-text'][normalize-space()='Calendar']").click()

    
    # Click menu Reports
    page.locator("//span[@class='menu-text'][normalize-space()='Reports']").click()
    # Click menu Sales
    page.locator("//span[@class='sub-menu-text'][normalize-space()='Sales']").click()
    # Click menu Expenses
    page.locator("//span[@class='sub-menu-text'][normalize-space()='Expenses']").click()
    # Click menu Expenses vs Income
    page.locator("//span[@class='sub-menu-text'][normalize-space()='Expenses vs Income']").click()
    # Click menu Leads
    page.locator("//span[@class='sub-menu-text'][normalize-space()='Leads']").click()
    # Click menu Timesheets overview
    page.locator("//span[@class='sub-menu-text'][normalize-space()='Timesheets overview']").click()
    # Click menu KB Articles
    page.locator("//span[@class='sub-menu-text'][normalize-space()='KB Articles']").click()
    