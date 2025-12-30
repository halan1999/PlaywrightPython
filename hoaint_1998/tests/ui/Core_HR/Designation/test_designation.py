from pages.HRM.core_hr.designation.designation import Designation
import pytest

def test_case_1(page, logined_page):
    designation = Designation(page)
    designation._go_to_core_hr_designation()
    designation._create_designation(department_name="hoaint_department_01")
    designation._edit_designation(designation.last_designation_name)
    designation._delete_designation(designation.last_designation_name)

@pytest.mark.skip
def test_case_2(page, logined_page):
    designation = Designation(page)
    designation._go_to_core_hr_designation()
    designation._select_row_per_page("10")
    # designation._click_button_in_pagination_controls(2)
    # designation._click_button_in_pagination_controls("Previous")
    # designation._click_button_in_pagination_controls("Next")