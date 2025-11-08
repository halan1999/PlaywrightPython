# ĐỌc từ excel_reader import read_login_data
from utils.excel_reader import read_login_data
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
import pytest
from playwright.sync_api import expect
import os
# Lấy đường dẫn tuyệt đối đến file Excel

import os
from utils.excel_reader import read_login_data

# Lấy đường dẫn từ MaiNTH/data/login.xlsx
current_dir = os.path.dirname(os.path.abspath(__file__))
excel_file_path = os.path.join(current_dir, "..", "..", "data", "login.xlsx")




# Đọc dữ liệu từ file Excel
login_test_data = read_login_data(excel_file_path, "Sheet1")
@pytest.mark.parametrize("case_id, username, password, expected, errormessage", login_test_data)
def test_login_excel(page, case_id, username, password, expected, errormessage) -> None:
    login_page = LoginPage(page)
    # Step 1: Visit login page
    login_page.visit_login_page()
    # Step 2: Perform login action with data from Excel
    login_page.login(username, password)
    # Step 3: Verify outcome based on expected result from Excel
    if expected == "Pass":
        expect(page).to_have_url(InventoryPage.URL)
        print(f"Test Case {case_id}: Login successful as expected for user '{username}'")
    else:
        error_locator = page.locator("[data-test='error']")
        expect(error_locator).to_be_visible()
        if errormessage:
            expect(error_locator).to_contain_text(errormessage)