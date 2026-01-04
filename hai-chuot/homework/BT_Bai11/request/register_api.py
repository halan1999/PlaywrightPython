from utils.data_generator import DataGenerator

class RegisterAPI:
    def __init__(self, request_context):
        self.request_context = request_context
        self.endpoint = "/api/register"

    def __setup_payload(self):
        self.name = "Hải Chuột"
        self.email = DataGenerator.random_email("playwright")
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
        self.response = self.request_context.post(
            self.endpoint,
            data = self.payload
        )
    
    def verify_user_created(self):
        response_json = self.response.json()
        assert self.response.status == 201 
        assert response_json["msg"] == "Register successfully."