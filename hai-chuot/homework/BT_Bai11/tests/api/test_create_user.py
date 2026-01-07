from request.register_api import RegisterAPI
from request.login_api import LoginAPI
from request.me_api import MeAPI
from request.logout_api import LogoutAPI

class TestCreateUser:
    name_user = None
    email_user = None
    password_user = None
    access_token = None

    def test_1_register_user(self, request_context):
        register_api = RegisterAPI(request_context)
        register_api.send_request()
        register_api.validate_response()
        register_api.verify_user_created()

        TestCreateUser.name_user = register_api.name
        TestCreateUser.email_user = register_api.email
        TestCreateUser.password_user = register_api.password

    def test_2_login_user(self, request_context):
        login_api = LoginAPI(request_context, TestCreateUser.email_user, TestCreateUser.password_user)
        login_api.send_request()
        login_api.validate_response()
        login_api.verify_login_successful()
        TestCreateUser.access_token = login_api.access_token

    def test_3_get_me(self, request_context):
        me_api = MeAPI(request_context, TestCreateUser.access_token)
        me_api.send_request()
        me_api.validate_response()
        me_api.verify_information_user("name", TestCreateUser.name_user)
        me_api.verify_information_user("email", TestCreateUser.email_user)

    def test_4_logout_user(self, request_context):
        logout_api = LogoutAPI(request_context, TestCreateUser.access_token)
        logout_api.send_request()
        logout_api.validate_response()
        logout_api.verify_logout_successful()