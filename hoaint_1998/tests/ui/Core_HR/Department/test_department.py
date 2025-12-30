from pages.HRM.core_hr.department.department import Department
import pytest

@pytest.mark.skip
def test_case_1(page, logined_page):
    department = Department(page)
    department._go_to_core_hr_deparment()
    department._create_department()
    department._edit_department(department.last_record_name)
    department._delete_department(department.last_record_name)

def test_case_2(page, logined_page):
    department = Department(page)
    department._go_to_core_hr_deparment()
    department._select_row_per_page("25")
    department._click_button_in_pagination_controls(2)
    department._click_button_in_pagination_controls("Previous")
    department._click_button_in_pagination_controls("Next")

