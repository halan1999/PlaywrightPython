import allure
from pages.login_page import LoginPage

@allure.epic("API → UI")
@allure.feature("Auth")
@allure.story("Login with API registered user")

# Test login UI với user đã register qua API
def test_login_with_api_user(page, registered_user_api):
    page.goto("/sign-in")

    login_page = LoginPage(page)
    login_page.login(
        registered_user_api["email"],
        registered_user_api["password"]
    )

    assert login_page.is_login_success(), \
        "Login success message not displayed"