from playwright.sync_api import Page, expect
import time

def test_erp_dashboard(page: Page):
    # Navigate to https://hrm.anhtester.com/
    print("\nNavigate to the web")
    page.goto("https://hrm.anhtester.com/erp/login")

    # Login
    page.locator("#iusername").fill("admin_example")
    page.locator("#ipassword").fill("123456")
    page.locator("//span[contains(text(),'Login')]").click()
    print("Login successfully")

    # Điều hướng đến Core HR > Department
    page.locator("//a[normalize-space()='Core HR']").click()
    page.locator("//a[normalize-space()='Department']").click()
    
    yield page  

    page.close()
    print("End")

@pytest.mark.usefixtures("deparment_page")
class TestDepartment:
    departmentName = "Thanh Ngân"
    new_department_name = "Ngân Thanh"

    def test_add_department(self, deparment_page: Page):
        # Thêm phòng ban mới
        deparment_page.locator("//input[@placeholder='Name']").fill(self.departmentName)
        deparment_page.locator("//span[normalize-space()='Save']").click()
        print("Add department successfully")

    def test_search_department(self, deparment_page: Page):
        deparment_page.locator("//input[@type='search']").fill(self.departmentName)
        deparment_page.wait_for_selector("#xin_table")  
        results = deparment_page.locator("//table//tbody//tr").count()
        if results > 0:
            first_cell = deparment_page.locator("//table[@id='xin_table']//tbody//tr[1]")
            expect(first_cell).to_contain_text(self.departmentName)
            print("Search successfully")
        else:
            print("Search failed")
    
    def test_update_department(self, deparment_page: Page):
        deparment_page.locator("//table[@id='xin_table']//tbody//tr[1]//span[@data-original-title='Edit']").click()
        deparment_page.wait_for_selector("#ajax_view_modal")
        deparment_page.locator("//div[@id='ajax_view_modal']//input[@name='department_name']").fill(self.new_department_name)
        deparment_page.locator("//div[@id='ajax_view_modal']//span[normalize-space()='Update']").click()
        print("Update department successfully")

    def test_delete_department(self, deparment_page: Page): 
        deparment_page.locator("//input[@type='search']").fill(self.new_department_name)
        deparment_page.locator("//input[@type='search']").press("Enter")
        deparment_page.locator("//table[@id='xin_table']//tbody//tr[1]//span[@data-original-title='Delete']").click()
        deparment_page.wait_for_selector("//form[@id='delete_record']")
        deparment_page.locator("//form[@id='delete_record']//button[normalize-space()='Confirm']").click()
        print("Delete department successfully")
