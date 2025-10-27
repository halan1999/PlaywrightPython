from playwright.sync_api import Page, expect, Playwright
import re, time

def test_define_location(page: Page):
    page.goto("https://the-internet.herokuapp.com/tables")

    lastname = page.locator("//table[@id='table1']//td[text()='Bach']")
    due = page.locator("//table[@id='table1']//td[text()='Bach']/following-sibling::td[3]")

    print(f"Khách hàng {lastname} có số tiền nợ {due}")
    page.close()

def test_page_herokuapp(page: Page):
    page.goto("https://the-internet.herokuapp.com/challenging_dom")
    
    #xử lý button
    red_button = page.locator("a.button.alert")
    
    try:
        expect(red_button).to_be_visible()
        red_button.click()
    except Exception as e:
        print("There is no button 'qux' trên màn hình", e)
    finally:
        page.close()
