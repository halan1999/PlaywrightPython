from utils.randoms import *

class LoginPayload:
    def __init__(self, email, password="Test@123456"):
        self.email = email
        self.password = password

    def to_dict(self):
        return self.__dict__

class LoginResponse:
    def __init__(self, json_data):
        self.message = json_data.get("msg")
        self.access_token = json_data.get("accessToken")
        self.expires_in = json_data.get("exp")