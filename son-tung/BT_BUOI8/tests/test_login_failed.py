from BT_BUOI8.pages.login_page import LoginPage

def test_login_failed(page):
    login_page = LoginPage(page)

    # Open webpage and login
    login_page.goto()
    login_page.login("invalid_user")

    # Assert Error message popup
    login_page.assert_error_message_visible()