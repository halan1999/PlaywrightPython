class LogoutAPI:
    def __init__(self, request_context, access_token: str):
        self.request_context = request_context
        self.access_token = access_token
        self.endpoint = "/api/logout​"

    def send_request(self):
        self.response = self.request_context.delete(
            url = self.endpoint,
            headers = {
                "Authorization": f"Bearer {self.access_token}"
            }
        )

    def verify_logout_successful(self):
        assert self.response.status == 200
        response_json = self.response.json()
        assert response_json["msg"] == "Logout successfully."