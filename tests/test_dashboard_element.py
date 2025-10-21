from playwright.sync_api import Page, expect
def test_dashboard_element(page: Page):
    
    # Goto page
    page.goto("https://crm.anhtester.com/admin/authentication")
    # Login
    page.get_by_role("textbox", name="Email Address").fill("admin@example.com")
    page.get_by_role("textbox", name="Password").fill("123456")
    page.get_by_role("button", name="Login").click()
    #  Locator Menu
    #  Click menu Dashboard
    page.locator("//span[@class='menu-text'][normalize-space()='Dashboard']").click()
    print("Clicked on Dashboard menu")
    # Click search input box
    page.locator("//input[@id='search_input']").click()
    # Click icon search
    page.locator("//span[@class='fa fa-search']").click()
    # label text DasInvoices Awaiting Payment
    page.locator("//span[@class='tw-truncate'][normalize-space()='Invoices Awaiting Payment']").text_content()
    print("Found Invoices Awaiting Payment element")
    