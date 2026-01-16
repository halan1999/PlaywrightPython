import pytest
import json
import allure
from api.login_api import LoginAPI
from utils.api_assertions import (
    assert_login_success_response,
    assert_error_response,
)


# ========= Reader data =========
def load_user_data():
    with open("data/login_user.json", encoding="utf-8") as f:
        return json.load(f)
USER_DATA = load_user_data()

# ========= Tests =========
@allure.epic("API")
@allure.feature("Auth")
@allure.story("Login")

@pytest.mark.parametrize(
    "user_key, expected_status",
    [
        ("valid_login_user", 200),
        ("invalid_login_user_wrong_password", 400),
        ("invalid_login_user_nonexistent_email", 404),
        ("invalid_login_user_blank_email", 422),
        ("invalid_login_user_blank_password", 400),
    ]
)
def test_login_user(api_context, user_key, expected_status):
    login_api = LoginAPI(api_context)
    payload = USER_DATA[user_key]

    response = login_api.login_user(payload)

    if expected_status == 200:
        assert_login_success_response(response)
    else:
        assert_error_response(response, expected_status)
 
