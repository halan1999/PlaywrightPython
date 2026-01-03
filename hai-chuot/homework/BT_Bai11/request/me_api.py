class MeAPI:
    def __init__(self, request_context, access_token: str):
        self.request_context = request_context
        self.access_token = access_token
        self.endpoint = "/api/me"
        self.key_profile = ["name", "email", "avatarUrl", "phone", "address"]

    def send_request(self):
        self.response = self.request_context.get(
            url=self.endpoint,
            headers={
                "Authorization": f"Bearer {self.access_token}"
            }
        )

    def verify_get_me_successful(self):
        assert self.response.status == 200
        response_json = self.response.json()
        assert "id" in response_json

    def verify_information_user(self, key: str, value: str):
        response_json = self.response.json()
        if key not in self.key_profile:
            raise ValueError(f"Key '{key}' is not valid. Valid keys are: {self.key_profile}")
        else:
            assert response_json[key] == f"{value}"
        
