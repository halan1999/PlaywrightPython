from core.base_request import BaseRequest
from core.base_request import APIMethod

class LoginAPI(BaseRequest):
    def __init__(self, request_context, email: str, password: str):
        super().__init__(request_context)
        self.email = email
        self.password = password
        self.access_token = None
        self.endpoint = "/api/login"

    def send_request(self):
        response = self._send_request(
            APIMethod.POST,
            self.endpoint,
            data = {
                "email": f"{self.email}",
                "password": f"{self.password}"
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
                },
                "accessToken": {
                    "type": "string"
                },
                "exp": {
                    "type": "string"
                }
            },
            "required": [
                "msg",
                "accessToken",
                "exp"
            ],
            "additionalProperties": False
        }

        self._validate_json_schema(self.response_json, expected_schema)

    def verify_login_successful(self):
        assert self.response_json["msg"] == "Login successfully."

        self.access_token = self.response_json["accessToken"]
