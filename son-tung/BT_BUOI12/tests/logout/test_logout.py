from BT_BUOI8.pages.login.login_page import LoginPage

def test_logout(page):
    login_page = LoginPage(page)

    # Login
    login_page.login("valid_user")
    login_page.assert_login_successful()

    # Log out
    login_page.logout()