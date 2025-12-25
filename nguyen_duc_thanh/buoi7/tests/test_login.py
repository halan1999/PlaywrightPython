
import allure


@allure.epic("HRM Anh Tester")
@allure.feature("Authentication")
@allure.story("Login")

@allure.title("Login success with valid credentials")
@allure.description("Verify user can login and see dashboard.")
@allure.severity(allure.severity_level.CRITICAL)
def test_login_successfully(login_page):
    creds = login_page.get_credential()
    with allure.step("Fill username/password and submit"):
        login_page.login(creds["valid_user"]["username"], creds["valid_user"]["password"])
    with allure.step("Assert login successfully"):
        login_page.assert_login_successful()

@allure.title("Login unsuccess with invalid credentials")
@allure.description("Verify user cannot login and see dashboard.")
@allure.severity(allure.severity_level.CRITICAL)
def test_login_failed(login_page):
    creds = login_page.get_credential()
    with allure.step("Fill username/password and submit"):
        login_page.login(creds["invalid_user"]["username"], creds["invalid_user"]["password"])
    with allure.step("Assert login unsuccessfully"):
        login_page.assert_login_failed()
