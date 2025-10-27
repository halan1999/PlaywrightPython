from playwright.sync_api import Page, expect, Playwright
import re, time

def test_login(page: Page):
    page.goto("https://crm.anhtester.com/admin/")

    page.locator("#email").fill("admin@example.com")
    page.locator("#password").fill("123456")
    page.get_by_role("button", name="Login").click()

    print("✅ Đăng nhập thành công!")

def test_define_elements_Main_menu(page: Page):
    # Kiểm tra đã login thành công và thấy Dashboard
    expect(page.get_by_text("Dashboard")).to_be_visible()
    expect(page).to_have_url("https://crm.anhtester.com/admin")

    # page.locator(".menu-text")
    # page.get_by_text("Dashboard")
    # Xác định các locator của main menu
    page.locator("//span[@class='menu-text' and normalize-space()='Dashboard']")
    page.locator("//span[@class='menu-text' and normalize-space()='Customers']")
    page.locator("//span[@class='menu-text' and normalize-space()='Sales']")
    page.locator("//span[@class='menu-text' and normalize-space()='Subscriptions']")
    page.locator("//span[@class='menu-text' and normalize-space()='Expenses']")
    page.locator("//span[@class='menu-text' and normalize-space()='Contracts']")
    page.locator("//span[@class='menu-text' and normalize-space()='Projects']")
    page.locator("//span[@class='menu-text' and normalize-space()='Tasks']")
    page.locator("//span[@class='menu-text' and normalize-space()='Support']")
    page.locator("//span[@class='menu-text' and normalize-space()='Leads']")
    page.locator("//span[@class='menu-text' and normalize-space()='Estimate Request']")
    page.locator("//span[@class='menu-text' and normalize-space()='Knowledge Base']")
    page.locator("//span[@class='menu-text' and normalize-space()='Utilities']")
    page.locator("//span[@class='menu-text' and normalize-space()='Reports']")

def test_define_locator_Dash(page: Page):
    page.locator("//span[@class='menu-text' and normalize-space()='Dashboard']").click()
    print("Hiển thị các items con của Dash")

    page.locator("//span[@class='tw-truncate' and normalize-space()='Invoices Awaiting Payment']")
    page.locator("//span[@class='tw-truncate' and normalize-space()='Converted Leads']")
    page.locator("//span[@class='tw-truncate' and normalize-space()='Projects In Progress']")
    page.locator("//span[@class='tw-truncate' and normalize-space()='Tasks Not Finished']")

    page.locator("//span[@class='tw-font-medium' and normalize-space()='Invoice overview']")
    page.locator("//span[@class='tw-font-medium' and normalize-space()='Estimate overview']")
    page.locator("//span[@class='tw-font-medium' and normalize-space()='Proposal overview']")




