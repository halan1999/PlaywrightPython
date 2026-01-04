import pytest
from playwright.sync_api import sync_playwright
from faker import Faker
@pytest.fixture(scope="session")
def api_context():
    with sync_playwright() as p:
        request_context = p.request.new_context(
            base_url = "https://book.anhtester.com/swagger#tag/authentication-management",
            extra_http_headers={
                    "Accept": "application/json"
                }
        )
        yield request_context
        request_context.dispose()

@pytest.fixture
def register(api_context):
    fake = Faker()
    payload = {
        "name": fake.name(),
        "email": fake.email(),
        "password": "123456",
        "avatarUrl": "",
        "phone": fake.phone_number(),
        "address": fake.address()
    }
    res = api_context.post("/api/register", data=payload)
    yield {
        "email": payload["email"],
        "password": payload["password"]
    }

@pytest.fixture
def login(api_context,register):
    payload = {
        "email": register["email"],
        "password": register["password"]
    }
    res = api_context.post("/api/login", data=payload)
    data = res.json()
    yield data["accessToken"]