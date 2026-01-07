from core.base_request import BaseRequest
from core.base_request import APIMethod

class MeAPI(BaseRequest):
    def __init__(self, request_context, access_token: str):
        super().__init__(request_context)
        self.access_token = access_token
        self.endpoint = "/api/me"
        self.key_profile = ["name", "email", "avatarUrl", "phone", "address"]

    def send_request(self):
        response = self._send_request(
            APIMethod.GET,
            self.endpoint,
            headers={
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
                "id": {
                    "type": "string"
                },
                "name": {
                    "type": "string"
                },
                "email": {
                    "type": "string"
                },
                "avatarUrl": {
                    "type": "string"
                },
                "phone": {
                    "type": "string"
                },
                "address": {
                    "type": "string"
                },
                "config": {
                    "type": "object"
                }
            },
            "required": [
                "id",
                "name",
                "email",
                "avatarUrl",
                "phone",
                "address"
            ],
            "additionalProperties": False
        }

        self._validate_json_schema(self.response_json, expected_schema)

    def verify_information_user(self, key: str, value: str):
        if key not in self.key_profile:
            raise ValueError(f"Key '{key}' is not valid. Valid keys are: {self.key_profile}")
        else:
            assert self.response_json[key] == value
        
