
def test_change_avatar(logged_in_module):
    page, login_page = logged_in_module
    page.goto("https://hrm.anhtester.com/erp/profile")
    # bước đổi avatar...
    login_page._take_screenshot("avatar_changed")


def test_change_password(logged_in_module):
    page, login_page = logged_in_module
    page.goto("https://hrm.anhtester.com/erp/change-password")
    # bước đổi password...
    login_page._take_screenshot("pwd_changed")


def test_view_activity_logs(logged_in_module):
    page, login_page = logged_in_module
    page.goto("https://hrm.anhtester.com/erp/activity")
    # bước verify logs...
    login_page._take_screenshot("activity_logs")
