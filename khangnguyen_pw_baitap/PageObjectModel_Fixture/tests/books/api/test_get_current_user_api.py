import allure
from data.books.api_payload.register_payload import build_register_payload
from data.books.api_payload.login_payload import build_login_payload
from utils.save_books_credentials import save_books_login_credential

@allure.title("Get current user information successfully")
@allure.description("Verify Get Current User Information API works appropriately")
def test_get_current_user_success(api_context):
    # Create register body payload
    with allure.step("Create register payload"):
        register_payload = build_register_payload()

    # Send API to register
    with allure.step("Register new account"):
        api_context.post("/api/register", data=register_payload)

    # Save new credentials
    with allure.step("Store login credentials to JSON file"):
        save_books_login_credential(
            email=register_payload["email"],
            password=register_payload["password"]
        )
        
    # Create login body payload
    with allure.step("Create login payload"):
        login_payload = build_login_payload(
            email=register_payload["email"],
            password=register_payload["password"]
        )

    # Send API to login and get access token
    with allure.step("Login and get access token"):
        login_response = api_context.post("/api/login", data=login_payload)
        token = login_response.json().get("accessToken")

    # Send API to get current user information
    with allure.step("Send GET /api/me"):
        response = api_context.get(
            "/api/me",
            headers={"authorization": f"Bearer {token}"}
        )

    # Verify status code is 200
    with allure.step("Verify status code is 200"):
        assert response.status == 200
    # Verify response payload matches register information
    with allure.step("Verify response"):
        body = response.json()
        assert body.get("name") == register_payload.get("name")
        assert body.get("email") == register_payload.get("email")
        assert body.get("address") == register_payload.get("address")