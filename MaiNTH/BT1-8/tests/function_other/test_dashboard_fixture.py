import pytest
from playwright.sync_api import Page, Playwright, sync_playwright, expect

@pytest.fixture
def login_page(playwright: Playwright) -> Page:
    # 1.Setup trước khi test run
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
    # Đảm bảo loin thành công
    expect(page).to_have_url("https://hrm.anhtester.com/erp/desk")
    print("1.Login successfully")
    # 2. Trả về page đã login để test sử dụng
    yield page
    # 3. Teardown sau khi test kết thúc
    context.close()
    browser.close()


def test_department_flow(login_page: Page) -> None:
    # Navigate to Department module
    login_page.get_by_role("link", name="Core HR").click()
    login_page.get_by_role("link", name="Department").click()
    # Add Departments
    login_page.get_by_role("textbox", name="Name").click()
    login_page.get_by_role("textbox", name="Name").fill("MaiNTH_test_1")
    login_page.get_by_role("button", name="Save").click()
    login_page.get_by_role("textbox", name="Name").click()
    login_page.get_by_role("textbox", name="Name").fill("MaiNTH_test_2")
    login_page.get_by_role("button", name="Save").click()
    print("2. Added Departments successfully")
    # Search and Update Department
    login_page.get_by_role("searchbox", name="Search").click()
    login_page.get_by_role("searchbox", name="Search").fill("MaiNTH_test_1")
    # verify search result
    login_page.get_by_text("MaiNTH_test_1").is_visible()
    print("3. Searched Department successfully")
    # Edit Department
    login_page.get_by_role("button", name="").click()
    login_page.locator("#edit_department").get_by_role("textbox", name="Name").click()
    login_page.locator("#edit_department").get_by_role("textbox", name="Name").fill("MaiNTH_test_1_update")
    login_page.get_by_role("button", name="Update").click()
    print("4. Edited Department successfully")
    # Search updated Department
    login_page.get_by_role("searchbox", name="Search").click()
    login_page.get_by_role("searchbox", name="Search").fill("MaiNTH_test_1_update")
    # verify search result
    login_page.get_by_text("MaiNTH_test_1_update").is_visible()
    print("5. Searched updated Department successfully")
    # Delete Departments
    login_page.get_by_role("button", name="").click()
    login_page.get_by_role("button", name="Confirm").click()
    print("6.Deleted Department 1 successfully")
    # Search to verify deletion
    # login_page.get_by_role("searchbox", name="Search").click()
    # login_page.get_by_role("searchbox", name="Search").fill("MaiNTH_test_1_update")
    # verify no result found
    no_data_text = login_page.locator("//td[@class='dataTables_empty']")
    expect(no_data_text).to_have_text("No records available")
    print("7. Verified deletion of Department successfully")  

    



 