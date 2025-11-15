
def test_login_successfully(login_page):
    creds = login_page.get_credential()
    login_page.login(creds["valid_user"]["username"], creds["valid_user"]["password"])
    login_page.assert_login_successful()
   
def test_login_failed(login_page):
    creds = login_page.get_credential()
    login_page.login(creds["invalid_user"]["username"], creds["invalid_user"]["password"])
    login_page.assert_login_failed()
