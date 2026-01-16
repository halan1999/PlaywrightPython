# components/api/profile_api.py
from api.base_api import BaseAPI
class ProfileAPI(BaseAPI):
    ENDPOINT = "/api/profile"

    def get_profile(self, endpoint):
        return super().get(endpoint)
    
    def update_profile(self, payload):
        return self.patch(
            self.ENDPOINT,
            data=payload
        )