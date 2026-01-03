from request.register_api import RegisterAPI
from request.login_api import LoginAPI
from request.me_api import MeAPI
from request.logout_api import LogoutAPI

class TestCreateUser:
    def test_1_register_user(self, request_context):
        register_api = RegisterAPI(request_context)
        register_api.send_request()
        register_api.verify_user_created()

        self.name_user = register_api.name
        self.email_user = register_api.email
        self.password_user = register_api.password

    # def test_2_login_user(self, request_context):
    #     login_api = LoginAPI(request_context, self.email_user, self.password_user)
    #     login_api.send_request()
    #     self.access_token = login_api.verify_login_successful()

    # def test_3_get_me(self, request_context):
    #     me_api = MeAPI(request_context, self.access_token)
    #     me_api.send_request()
    #     me_api.verify_get_me_successful()
    #     me_api.verify_information_user("name", self.name_user)
    #     me_api.verify_information_user("email", self.email_user)

    # def test_4_logout_user(self, request_context):
    #     logout_api = LogoutAPI(request_context, self.access_token)
    #     logout_api.send_request()
    #     logout_api.verify_logout_successful()