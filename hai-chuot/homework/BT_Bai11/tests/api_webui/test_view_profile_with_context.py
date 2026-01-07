from request.register_api import RegisterAPI
from request.login_api import LoginAPI
from pages.profile_page import ProfilePage
import time

class TestCreateUser:
    name_user = None
    email_user = None
    password_user = None
    access_token = None

    def test_1_register_user(self, initial_context):
        register_api = RegisterAPI(initial_context)
        register_api.send_request()
        register_api.validate_response()
        register_api.verify_user_created()

        TestCreateUser.name_user = register_api.name
        TestCreateUser.email_user = register_api.email
        TestCreateUser.password_user = register_api.password

    def test_2_login_user(self, initial_context):
        login_api = LoginAPI(initial_context, TestCreateUser.email_user, TestCreateUser.password_user)
        login_api.send_request()
        login_api.validate_response()
        login_api.verify_login_successful()
        TestCreateUser.access_token = login_api.access_token

    def test_3_view_profile(self, initial_page_with_storage_state):
        profile_page = ProfilePage(initial_page_with_storage_state, "https://book.anhtester.com")
        profile_page.navigate_to_profile()
        time.sleep(10)
        # profile_page.verify_name(TestCreateUser.name_user)