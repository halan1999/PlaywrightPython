from api.profile_api import ProfileAPI
from utils.data_loader import load_json_data
from utils.api_assertions import (
    assert_status_code,
    assert_profile_data
)

PROFILE_DATA = load_json_data("profile_data.json")

def test_update_profile_success(api_context_authenticated):
    api = ProfileAPI(api_context_authenticated)

    payload = PROFILE_DATA["success_update_profile"]
    response = api.update_profile(payload)

    assert_status_code(response, 200)

    data = response.json()
    assert_profile_data(data, payload)

def test_update_profile_blank_name(api_context_authenticated):
    api = ProfileAPI(api_context_authenticated)

    payload = PROFILE_DATA["validate_update_profile_blank_name"]
    response = api.update_profile(payload)

    assert_status_code(response, 200)  # backend accept