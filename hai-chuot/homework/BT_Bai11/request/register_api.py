from utils.data_generator import DataGenerator
from core.base_request import BaseRequest
from core.base_request import APIMethod

class RegisterAPI(BaseRequest):
    def __init__(self, request_context):
        super().__init__(request_context)
        self.endpoint = "/api/register"
        self.name = None
        self.email = None
        self.password = None
        self.payload = None

    def __setup_payload(self):
        self.name = DataGenerator.generate_name()
        self.email = DataGenerator.generate_email()
        self.password = "12345678"
        self.payload = {
            "name": f"{self.name}",
            "email": f"{self.email}",
            "password": f"{self.password}",
            "avatarUrl": "",
            "phone": "",
            "address": ""
        }

    def send_request(self):
        self.__setup_payload()
        response = self._send_request(
            APIMethod.POST,
            self.endpoint,
            data = self.payload
        )

        self.response_code = response.status
        self.response_json = self._get_response_body(response)

    def validate_response(self):
        self._verify_status_code(self.response_code, 201)
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
    
    def verify_user_created(self):
        assert self.response_json["msg"] == "Register successfully."