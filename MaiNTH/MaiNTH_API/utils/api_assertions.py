# ============= Hàm chứa các hàm assertion dùng chung cho API tests=========

# Hàm check status code
def assert_status_code(response, expected_status):
    assert response.status == expected_status, \
        f"Expected status {expected_status}, got {response.status}"

# Hàm check login success response
def assert_login_success_response(response):
    assert_status_code(response, 200)

    body = response.json()

    # Login success: phải có accessToken
    assert "accessToken" in body, f"Missing accessToken in response: {body}"

# Hàm check register success response
def assert_register_success_response(response):
    assert response.status == 201
    body = response.json()

    assert "msg" in body
    assert body["msg"] == "Register successfully."

# Hàm check error response
def assert_error_response(response, expected_status):
    assert_status_code(response, expected_status)

    body = response.json()

    assert "msg" in body, f"Missing 'msg' in error response: {body}"

    # fields: optional nhưng nếu có thì phải đúng type
    if "fields" in body:
        assert isinstance(body["fields"], dict), \
            f"'fields' must be dict: {body}"
        
# Hàm check profile data response
def assert_profile_data(response_data, expected_payload):
    # Backend chỉ trả msg
    assert "msg" in response_data, "Response missing 'msg'"
    assert response_data["msg"] == "Updated profile successfully."

# Hàm check get me data response
def assert_getme_data(data):
    expected_fields = [
        "id",
        "name",
        "email",
        "phone",
        "address",
        "avatarUrl",
        "config"
    ]

    for field in expected_fields:
        assert field in data, f"Missing field '{field}' in get me response"

    assert isinstance(data["id"], str)
    assert isinstance(data["name"], str)
    assert isinstance(data["email"], str)
    assert isinstance(data["phone"], str)
    assert isinstance(data["address"], str)
    assert isinstance(data["avatarUrl"], (str, type(None)))
    assert isinstance(data["config"], dict)

