import allure
from data.books.api_payload.register_payload import build_register_payload
from utils.save_books_credentials import save_books_login_credential

REGISTER_SUCCESSFUL_MESSAGE = "Register successfully."

@allure.title("Register new account successfully")
@allure.description("Verify that Register API works appropriately")
def test_register_new_account(api_context):
    # Create register body payload
    with allure.step("Create register payload"):
        register_payload = build_register_payload()

    # Send API to register
    with allure.step("Send POST /api/register"):
        register_response = api_context.post("/api/register", data=register_payload)

    # Verify status code is 201
    with allure.step("Verify status code is 201"):
        assert register_response.status == 201

    # Verify message in response payload
    with allure.step("Verify response"):
        assert register_response.json().get("msg") == REGISTER_SUCCESSFUL_MESSAGE

    # Save new credentials
    with allure.step("Store login credentials to JSON file"):
        save_books_login_credential(
            email=register_payload["email"],
            password=register_payload["password"]
        )