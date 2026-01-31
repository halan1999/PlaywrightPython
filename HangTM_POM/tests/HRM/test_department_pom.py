from pages.HRM.login_page import LoginPage
from pages.HRM.department_page import DepartmentPage

def test_add_department_pom(hrm_logged_in_page):
    page=hrm_logged_in_page
    Department_page=DepartmentPage(page)
    Department_page.open_department_page()
#add:
    department_name="Test Department_POM"
    Department_page.add_department(department_name)
#search:
    Department_page.search_department(department_name)
#verify search result:
    assert Department_page.is_department_present(department_name)



 