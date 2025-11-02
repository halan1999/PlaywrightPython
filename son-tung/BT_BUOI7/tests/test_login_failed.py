from BT_BUOI7.pages.login_page import LoginPage

def test_add_to_cart(page):
    login_page = LoginPage(page)

    # Open webpage and login
    login_page.goto()
    login_page.login("locked_out_user", "secret_sauce")
    login_page.assert_error_message_visible()