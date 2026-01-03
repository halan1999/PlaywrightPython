class ProfileAPI:

    def __init__(self, request_context, access_token: str):
        self.request_context = request_context
        self.endpoint = "/api/profile"
        self.access_token = access_token
        self.key_profile = ["name", "email", "avatarUrl", "phone", "address"]

    def change_password(self, old_password: str, new_password: str):
        self.response = self.request_context.patch(
            url = self.endpoint,
            data = {
                "password": f"{new_password}",
                "password_old": f"{old_password}"
            },
            headers = {
                "Authorization": f"Bearer {self.access_token}"
            }
        )

    def update_profile(self, information_change: dict):
        for key in information_change.keys():
            if key not in self.key_profile:
                raise ValueError(f"Key '{key}' is not valid. Valid keys are: {self.key_profile}")
        
        self.response = self.request_context.patch(
                url = self.endpoint,
                data = information_change,
                headers = {
                    "Authorization": f"Bearer {self.access_token}"
                }
            )

    def verify_update_profile_successful(self) -> str:
        assert self.response.status == 200
        response_json = self.response.json()
        assert response_json["msg"] == "Updated profile successfully."