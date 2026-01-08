from utils.randoms import *

class RefetchTokenrPayload:
    def __init__(self, access_token):
        self.headers = {
            "Authorization": f"Bearer {access_token}"
        }

    def to_dict(self):
        return self.__dict__

class RefetchTokenrResponse:
    def __init__(self, json_data):
        self.message = json_data.get("msg")
        self.acces_token = json_data.get("access_token")
        self.exp = json_data.get("exp")