class LoginAPI:
    def __init__(self, request_context, email: str, password: str):
        self.request_context = request_context
        self.email = email
        self.password = password
        self.endpoint = "/api/login"

    def send_request(self):
        self.response = self.request_context.post(
            url = self.endpoint,
            data = {
                "email": f"{self.email}",
                "password": f"{self.password}"
            }
        )

    def verify_login_successful(self) -> str:
        assert self.response.status == 200
        response_json = self.response.json()
        assert response_json["msg"] == "Login successfully."
        assert "accessToken" in response_json

        return response_json["accessToken"]
