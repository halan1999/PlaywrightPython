from playwright.sync_api import  Page, expect
import re, time

def test_crm_dropdown(page: Page):
    page.goto("https://crm.anhtester.com/admin/authentication")
    page.get_by_role("textbox", name="Email").click()
    page.get_by_role("textbox", name="Email").fill("admin@example.com")
    page.get_by_role("textbox", name="Password").fill("123456")
    page.get_by_role("button", name="Login").click()
    page.wait_for_load_state("networkidle")
    page.locator("//li[@class='menu-item-sales']").click()
    page.wait_for_selector("//li[@class='menu-item-sales active']")
    expect(page.locator("//ul[@class='nav nav-second-level collapse in']//span[@class='sub-menu-text']")).to_have_count(6)