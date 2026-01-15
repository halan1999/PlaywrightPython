import allure
from data.books.api_payload.register_payload import build_register_payload
from data.books.api_payload.login_payload import build_login_payload
from utils.save_books_credentials import save_books_login_credential

LOGIN_SUCCESSFUL_MESSAGE = "Login successfully."

@allure.title("Login successfully after registration")
@allure.description("Verify Login API works appropriately")
def test_login_success(api_context):
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

    # Send API to login
    with allure.step("Send POST /api/login"):
        login_response = api_context.post("/api/login", data=login_payload)

    # Verify status code is 200
    with allure.step("Verify status code is 200"):
        assert login_response.status == 200

    # Verify message in response payload
    with allure.step("Verify response"):
        body = login_response.json()
        assert body.get("msg") == LOGIN_SUCCESSFUL_MESSAGE
        assert body.get("accessToken")