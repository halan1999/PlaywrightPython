import time
from playwright.sync_api import sync_playwright

def test_create_and_search_department():
    Department_Name= "haodt2"
    with sync_playwright() as pw:
        browser = pw.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        # 1. Mở trang
        page.goto("https://hrm.anhtester.com/erp/login")

        # 2. Login (nếu có)
        page.fill("#iusername", "admin_example")
        page.fill("#ipassword", "123456")
        page.click("//button[@type='submit']")
        time.sleep(10)
    
        # 3. Đi đến trang quản lý đơn vị
        menu_locator = page.locator("//nav[@class='pc-sidebar light-sidebar']")
        menu_locator.evaluate("el => el.scrollTop = el.scrollHeight")  
        time.sleep(1)
        page.click("//a[normalize-space()='Core HR']")
        page.click("//a[normalize-space()='Department']")
        time.sleep(10)
        
        # Create department
        page.fill("//input[@placeholder='Name']", Department_Name)

        # 6. Submit form
        page.click("//div[@class='card-footer text-right']//button[@type='submit']")
        time.sleep(10)

        # Seach department
        page.fill("//input[@type='search']", Department_Name)
        time.sleep(10)

        # Check
        # 9. Lấy dòng đầu tiên của bảng
        first_row = page.locator("//td[contains(@class,'sorting_1')]").inner_text()

        # 10. Kiểm tra
        if "haodt1"in first_row:
            print("✔ Đơn vị đã được tạo và xuất hiện ở dòng 1!")
        else:
            print("✘ Không thấy đơn vị ở dòng 1!")
        browser.close()


if __name__ == "__main__":
    test_create_and_search_department()
