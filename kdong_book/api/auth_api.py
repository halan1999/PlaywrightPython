from core.api_client import APIClient
from config.env_config import EnvConfig

class AuthAPI(APIClient):
    def register_user(self,payload: dict):
        # Try 1: body phẳng như swagger
        res = self.request.post("/api/register", data=payload)
        if res.ok:
            return res.json()

        # Try 2: fallback - bọc "fields" (nếu backend yêu cầu schema kiểu này)
        res2 = self.request.post("/api/register", data={"fields": payload})
        if res2.ok:
            return res2.json()

        raise AssertionError(
            f"Register failed.\n"
            f"Try1: {res.status} - {res.text()}\n"
            f"Try2: {res2.status} - {res2.text()}"
        )
    