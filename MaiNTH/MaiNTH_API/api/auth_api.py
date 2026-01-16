from api.base_api import BaseAPI
class AuthAPI(BaseAPI):
  
    def __init__(self, api_context):
        super().__init__(api_context)

    def register(self, user_data: dict):
        return self.api_context.post(
            "/api/register",
            data=user_data
        )

    def login(self, email: str, password: str) -> str:
        response = self.api_context.post(
            "/api/login",
            data={
                "email": email,
                "password": password
            }
        )

        assert response.ok, f"Login failed: {response.text()}"
        return response.json()["accessToken"]