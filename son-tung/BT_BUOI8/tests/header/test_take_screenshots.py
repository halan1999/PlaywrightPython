def test_take_screenshots(login_page):
    # Login
    login_page.login_user("valid_user")
    login_page.assert_login_successful()

    # Click all button in header bar
    login_page.open_all_button_via_header()
    login_page.open_language_list_via_header()
    login_page.open_app_list_via_header()