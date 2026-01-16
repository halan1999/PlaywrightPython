# components/api/register_api.py
from api.base_api import BaseAPI
class RegisterAPI(BaseAPI):
    ENDPOINT = "/api/register"

    def register_user(self, payload):
        return self.post(
            self.ENDPOINT,
            data=payload
        )