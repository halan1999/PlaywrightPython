import allure
from data.books.api_payload.register_payload import build_register_payload
from data.books.api_payload.login_payload import build_login_payload
from utils.save_books_credentials import save_books_login_credential

LOGOUT_SUCCESS_MESSAGE = "Logout successfully."

@allure.title("Logout successfully")
@allure.description("Verify Log Out API works appropriately")
def test_logout(api_context):
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

    # Verify access token is not null or empty
    with allure.step("Verify access token is valid"):
        assert token is not None
        assert token != ""

    # Send API to logout
    with allure.step("Send DELETE /api/logout"):
        logout_response = api_context.delete(
            "/api/logout",
            headers={"authorization": f"Bearer {token}"}
        )

    # Verify status code is 200
    with allure.step("Verify status code is 200"):
        assert logout_response.status == 200

    # Verify message in response payload
    with allure.step("Verify response"):
        body = logout_response.json()
        assert body.get("msg") == LOGOUT_SUCCESS_MESSAGE