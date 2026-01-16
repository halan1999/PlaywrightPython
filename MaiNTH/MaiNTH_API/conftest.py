import pytest
from playwright.sync_api import sync_playwright

from utils.data_factory.email_factory import generate_unique_email
from utils.data_factory.register_user_factory import build_register_user
from api.auth_api import AuthAPI

# ================= ROOT PLAYWRIGHT =================

@pytest.fixture(scope="session")
def playwright_instance():
    with sync_playwright() as p:
        yield p


# ================= API CONTEXT =================
@pytest.fixture(scope="session")
def api_context(playwright_instance):
    context = playwright_instance.request.new_context(
        base_url="https://book.anhtester.com",
        extra_http_headers={
            "Content-Type": "application/json"
        }
    )
    yield context
    context.dispose()

# ================ API CONTEXT AUTHENTICATED =================
# @pytest.fixture(scope="session")
# def api_context_authenticated(playwright_instance):
#     # context thường để login
#     context = playwright_instance.request.new_context(
#         base_url="https://book.anhtester.com",
#         extra_http_headers={
#             "Content-Type": "application/json"
#         }
#     )

#     response = context.post(
#         "/api/login",
#         data={
#             "email": "mainth1368@gmail.com",
#             "password": "password123"
#         }
#     )

#     token = response.json()["accessToken"]

#     # context đã authenticate
#     auth_context = playwright_instance.request.new_context(
#         base_url="https://book.anhtester.com",
#         extra_http_headers={
#             "Authorization": f"Bearer {token}",
#             "Content-Type": "application/json"
#         }
#     )

#     yield auth_context

#     auth_context.dispose()
#     context.dispose()

# ================ API CONTEXT NO COOKIE =================
@pytest.fixture
def api_context_no_cookie(playwright_instance):
    context = playwright_instance.request.new_context(
        base_url="https://book.anhtester.com"
    )
    yield context
    context.dispose()
#  ================= Tạo fixture register user cho UI test =================

@pytest.fixture
def registered_user_api(playwright_instance):
    context = playwright_instance.request.new_context(
        base_url="https://book.anhtester.com",
        extra_http_headers={"Content-Type": "application/json"}
    )

    # Lấy data từ factory (JSON + random email)
    user_data = build_register_user("valid_user_1")

    response = context.post(
        "/api/register",
        data=user_data  
    )

    assert response.status == 201, f"Register failed: {response.text()}"

    yield {
        "email": user_data["email"],
        "password": user_data["password"]
    }

    context.dispose()

# ================= API Fixture Register + Login =================

@pytest.fixture
def api_user(api_context):
    # Tạo user mới
    auth_api = AuthAPI(api_context)
    # Lấy data từ factory
    user = build_register_user("valid_user_1")
    # Đăng ký và đăng nhập
    auth_api.register(user)
    token = auth_api.login(user["email"], user["password"])
    # Trả về thông tin user và token
    yield {
        "email": user["email"],
        "password": user["password"],
        "token": token
    }

# ================ API CONTEXT AUTHENTICATED =================
@pytest.fixture
def api_context_authenticated(playwright_instance, api_user):
    context = playwright_instance.request.new_context(
        base_url="https://book.anhtester.com/sign-in",
        extra_http_headers={
            "Authorization": f"Bearer {api_user['token']}",
            "Content-Type": "application/json"
        }
    )
    yield context
    context.dispose()

   


# ================= UI PAGE CONTEXT =================
@pytest.fixture(scope="session")
def page (playwright_instance):
    browser = playwright_instance.chromium.launch(headless=False)
    context = browser.new_context(
        base_url="https://book.anhtester.com/sign-in"
    )
    page  = context.new_page()
    yield page
    context.close()
    browser.close()
