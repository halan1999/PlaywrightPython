import allure
from data.books.api_payload.register_payload import build_register_payload
from data.books.api_payload.login_payload import build_login_payload
from data.books.api_payload.profile_payload import build_profile_payload
from utils.save_books_credentials import save_books_login_credential

UPDATE_SUCCESSFUL_MESSAGE = "Updated profile successfully."

@allure.title("Update user profile successfully")
@allure.description("Verify Update Profile API works appropriately")
def test_update_profile_success(api_context):
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

    # Create update profile body payload
    with allure.step("Create update profile payload"):
        update_payload = build_profile_payload(
            register_payload=register_payload,
            address="71 Hoang Van Thai, Tan My, Ho Chi Minh City"
        )

    # Send API to update profile information
    with allure.step("Send PATCH /api/profile"):
        update_response = api_context.patch(
            "/api/profile",
            data=update_payload,
            headers={"authorization": f"Bearer {token}"}
        )

    # Verify status code is 200
    with allure.step("Verify status code is 200"):
        assert update_response.status == 200

    # Verify message in response payload
    with allure.step("Verify response"):
        body = update_response.json()
        assert body.get("msg") == UPDATE_SUCCESSFUL_MESSAGE