from core.base_request import BaseRequest
from core.base_request import APIMethod

class ProfileAPI(BaseRequest):

    def __init__(self, request_context, access_token: str):
        super().__init__(request_context)
        self.endpoint = "/api/profile"
        self.access_token = access_token
        self.key_profile = ["name", "email", "avatarUrl", "phone", "address"]

    def change_password(self, old_password: str, new_password: str):
        response = self._send_request(
            APIMethod.PATCH,
            self.endpoint,
            data = {
                "password": f"{new_password}",
                "password_old": f"{old_password}"
            },
            headers = {
                "Authorization": f"Bearer {self.access_token}"
            }
        )

        self.response_code = response.status
        self.response_json = self._get_response_body(response)

    def validate_response(self):
        self._verify_status_code(self.response_code, 200)
        expected_schema = {
            "type": "object",
            "properties": {
                "msg": {
                    "type": "string"
                }
            },
            "required": [
                "msg"
            ]
        }

        self._validate_json_schema(self.response_json, expected_schema)

    def update_profile(self, information_change: dict):
        for key in information_change.keys():
            if key not in self.key_profile:
                raise ValueError(f"Key '{key}' is not valid. Valid keys are: {self.key_profile}")
        
        response = self._send_request(
                APIMethod.PATCH,
                self.endpoint,
                data = information_change,
                headers = {
                    "Authorization": f"Bearer {self.access_token}"
                }
            )

        self.response_code = response.status
        self.response_json = self._get_response_body(response)

    def verify_update_profile_successful(self):
        assert self.response_json["msg"] == "Updated profile successfully."