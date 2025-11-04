from pages.login_page import LoginPage
def test_login_successfully(page):
    login_page = LoginPage(page)
    login_page.login("admin_example", "123456")
    login_page.assert_login_successful()

def test_login_failure(page):
    login_page = LoginPage(page)
    login_page.login("admin_example", "1234567")
    login_page.assert_login_failed()

def test_forgot_password(page):
    login_page = LoginPage(page)
    login_page.goto_forgot_password()
    login_page.assert_goto_forgot_password()