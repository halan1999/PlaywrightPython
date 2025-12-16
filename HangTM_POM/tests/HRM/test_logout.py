from pages.HRM.header_page import HeaderPage
from pages.HRM.login_page import LoginPage
def test_logout(hrm_logged_in_page):
    page=hrm_logged_in_page
    header=HeaderPage(page)
    header.logout()
    login_page=LoginPage(page)
    login_page.should_visible(login_page.username_input)

    

 