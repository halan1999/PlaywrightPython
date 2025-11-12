def test_login_invaliduser(login_page):
    login_page.goto()
    login_page.login_user("invalid_user")

def test_login_valid(login_page):
    login_page.goto()
    login_page.login_user("valid_user")













