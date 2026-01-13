from utils.randoms import *

class RegisterPayload:
    def __init__(self, name="kimqa", password="Test@123456"):
        self.name = random_name()
        self.email = random_email()
        self.password = password
        self.avatarUrl = ""
        self.phone = "0900000000"
        self.address = random_address()

    def to_dict(self):
        return self.__dict__

class RegisterResponse:
    def __init__(self, json_data):
        self.message = json_data.get("msg")