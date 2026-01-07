import pytest
from request.register_api import RegisterAPI
from request.login_api import LoginAPI
from pages.login_page import LoginPage

@pytest.mark.usefixtures("initial_context")
class TestCreateApiLoginUI:
    name_user = None
    email_user = None
    password_user = None
    access_token = None

    def test_1_register_user(self, initial_context):
        register_api = RegisterAPI(initial_context)
        register_api.send_request()
        register_api.validate_response()
        register_api.verify_user_created()

        TestCreateApiLoginUI.name_user = register_api.name
        TestCreateApiLoginUI.email_user = register_api.email
        TestCreateApiLoginUI.password_user = register_api.password

    def test_2_login_ui(self, initial_page):
        login_page = LoginPage(initial_page, "https://book.anhtester.com/sign-in")
        login_page.login(TestCreateApiLoginUI.email_user, TestCreateApiLoginUI.password_user)
        login_page.verify_login_successful()