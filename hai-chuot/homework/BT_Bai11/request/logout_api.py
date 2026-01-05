from core.base_request import BaseRequest
from core.base_request import APIMethod

class LogoutAPI(BaseRequest):
    def __init__(self, request_context, access_token: str):
        super().__init__(request_context)
        self.access_token = access_token
        self.endpoint = "/api/logout"

    def send_request(self):
        response = self._send_request(
            APIMethod.DELETE,
            self.endpoint,
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

    def verify_logout_successful(self):
        assert self.response_json["msg"] == "Logout successfully."