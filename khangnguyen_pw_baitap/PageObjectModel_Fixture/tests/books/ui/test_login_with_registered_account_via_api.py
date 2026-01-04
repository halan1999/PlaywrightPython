import allure
from data.books.api_payload.register_payload import build_register_payload
from api.register_api import register_user
from pages.books.login_page import LoginPage
from components.books.left_menu import LeftMenu

@allure.title("Login with account registered via API")
@allure.description("Register account via API and login successfully via UI")
def test_login_with_account_registered_via_api(page, api_context):

    with allure.step("Register account via API"):
        register_user(api_context, build_register_payload())

    with allure.step("Login via UI and verify success"):
        login_page = LoginPage(page)
        login_page.open()
        login_page.login_valid()
        assert LeftMenu(page).is_left_menu_visible()