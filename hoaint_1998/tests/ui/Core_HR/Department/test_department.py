from pages.HRM.core_hr.department.department import Department

def test_case_1(page, logined_page):
    department = Department(page)
    department._go_to_core_hr_deparment()
    department._create_department()