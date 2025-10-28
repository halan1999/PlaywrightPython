from playwright import sync_api, page, expect
import re
def test_open_page(page:page.Page):
    page.goto("https://hrm.anhtester.com/erp/login")
    page.get_by_placeholder("Your username").fill("admin")
    page.get_by_placeholder("Enter Password").fill("123456")
    page.get_by_role("button", name="Login").click()
    user_login_page=page.locator("//span[@class='user-name' and normalize-space()='admin_example hello']")
    expect(user_login_page).to_be_visible()
    page.locator("//a[contains(@class,'pc-link') and contains(@class,'sidenav-toggle') and contains(normalize-space(.), 'Core HR')]").click()
    page.locator("//a[contains(@class,'pc-link') and contains(@href, '/erp/departments-list')]").click()
    # deparment mới
    dep_name="Trần Minh Hằng"
    page.locator("//input[@placeholder='Name']").fill(dep_name)
    page.get_by_role("button", name="Save").click()
    # Verify new department displayed in the Department table
    new_department=page.locator(f"//table//tr[td[normalize-space()='{dep_name}']]")
    expect(new_department).to_be_visible()
    # Search function:
    text_input="Hằng"
    search_box=page.locator("//input[@type='search' and @aria-controls='xin_table']")
    search_box.fill(text_input)
    page.wait_for_timeout(500)
    cells=page.locator("//table[@id='xin_table'//tbody/tr/td[1])]")
    row_count=cells.count()
    assert row_count>0, "No records found in the table after search."
    for i in range(row_count):
        cell_text = cells.nth(i).inner_text().strip()
        print(f"Hàng {i+1}: {cell_text}")
        assert text_input.lower() in cell_text.lower(), (
            f"Dòng {i+1} = '{cell_text}' KHÔNG chứa '{text_input}' sau khi search"
        )