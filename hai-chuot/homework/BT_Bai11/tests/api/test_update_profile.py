from request.register_api import RegisterAPI
from request.login_api import LoginAPI
from request.profile_api import ProfileAPI
from request.me_api import MeAPI
from utils.data_generator import DataGenerator

class TestUpdateProfile:
    name_user = None
    email_user = None
    password_user = None
    access_token = None
    information_change = {
        "name": "Hải Chuột",
        "phone": DataGenerator.generate_phone()
    }

    def test_1_register_user(self, request_context):
        register_api = RegisterAPI(request_context)
        register_api.send_request()
        register_api.validate_response()
        register_api.verify_user_created()

        TestUpdateProfile.name_user = register_api.name
        TestUpdateProfile.email_user = register_api.email
        TestUpdateProfile.password_user = register_api.password

    def test_2_login_user(self, request_context):
        login_api = LoginAPI(request_context, TestUpdateProfile.email_user, TestUpdateProfile.password_user)
        login_api.send_request()
        login_api.validate_response()
        login_api.verify_login_successful()
        TestUpdateProfile.access_token = login_api.access_token

    def test_3_update_profile(self, request_context):
        profile_api = ProfileAPI(request_context, TestUpdateProfile.access_token)
        profile_api.update_profile(TestUpdateProfile.information_change)
        profile_api.validate_response()
        profile_api.verify_update_profile_successful()

    def test_4_get_me(self, request_context):
        me_api = MeAPI(request_context, TestUpdateProfile.access_token)
        me_api.send_request()
        me_api.validate_response()
        me_api.verify_information_user("name", TestUpdateProfile.information_change["name"])
        me_api.verify_information_user("phone", TestUpdateProfile.information_change["phone"])