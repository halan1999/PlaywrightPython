import pytest
import json
import allure

from api.register_api import RegisterAPI
from utils.api_assertions import (
    assert_register_success_response,
    assert_error_response
)
from utils.data_factory.email_factory import generate_unique_email

# ========= Reader data =========
def load_user_data():
    with open("data/register_user.json", encoding="utf-8") as f:
        return json.load(f)


USER_DATA = load_user_data()

# ========= Tests =========
@allure.epic("API")
@allure.feature("Auth")
@allure.story("Register")

@pytest.mark.parametrize(
    "user_key, expected_status",
    [
        ("valid_user_1", 201),
        ("valid_user_2", 201),
        ("valid_user_3", 201),
        ("valid_user_4", 201),
        ("invalid_user_blank", 422),
        ("invalid_email_blank", 422),
        ("invalid_pw_blank", 400),
        ("invalid_email_format", 422),
    ]
)
def test_register_user(api_context, user_key, expected_status):
    # Khởi tạo RegisterAPI
    register_api = RegisterAPI(api_context)
    # Lấy data test từ file JSON và copy để chạy độc lập
    payload = USER_DATA[user_key].copy()   # ✅ QUAN TRỌNG

    # Chỉ generate email tự động cho case hợp lệ
    if expected_status == 201 and "{{random_email}}" in payload.get("email", ""):
        payload["email"] = payload["email"].replace(
            "{{random_email}}",
            generate_unique_email(user_key)
        )
    # Gửi request đăng ký
    response = register_api.register_user(payload)
    # Kiểm tra kết quả
    if expected_status == 201:
        assert_register_success_response(response)
    else:
        assert_error_response(response, expected_status)



    


