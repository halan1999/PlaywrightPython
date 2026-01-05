from request.register_api import RegisterAPI
from request.login_api import LoginAPI
from request.profile_api import ProfileAPI
from request.logout_api import LogoutAPI

class TestChangePassword:
    name_user = None
    email_user = None
    password_user = None
    access_token = None
    new_password = "Abc@1234"

    def test_1_register_user(self, request_context):
        register_api = RegisterAPI(request_context)
        register_api.send_request()
        register_api.validate_response()
        register_api.verify_user_created()

        TestChangePassword.name_user = register_api.name
        TestChangePassword.email_user = register_api.email
        TestChangePassword.password_user = register_api.password

    def test_2_login_user(self, request_context):
        login_api = LoginAPI(request_context, TestChangePassword.email_user, TestChangePassword.password_user)
        login_api.send_request()
        login_api.validate_response()
        login_api.verify_login_successful()
        TestChangePassword.access_token = login_api.access_token

    def test_3_change_password(self, request_context):
        profile_api = ProfileAPI(request_context, TestChangePassword.access_token)
        profile_api.change_password(TestChangePassword.password_user, TestChangePassword.new_password)
        profile_api.validate_response()
        profile_api.verify_update_profile_successful()

    def test_4_login_user_with_new_password(self, request_context):
        login_api = LoginAPI(request_context, TestChangePassword.email_user, TestChangePassword.new_password)
        login_api.send_request()
        login_api.validate_response()
        login_api.verify_login_successful()