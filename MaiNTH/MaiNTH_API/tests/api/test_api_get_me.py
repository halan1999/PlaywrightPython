import  pytest
import  allure
from api.getme_api import GetMeAPI
from utils.api_assertions import (
    assert_status_code,
    assert_getme_data
)

@allure.epic("API")
@allure.feature("User")
@allure.story("Get Me")
def test_get_me_success(api_context_authenticated):
    getme_api = GetMeAPI(api_context_authenticated)

    response = getme_api.get_me()

    assert_status_code(response, 200)

    data = response.json()
    assert_getme_data(data)

def test_get_me_unauthorized(api_context):
    getme_api = GetMeAPI(api_context)

    response = getme_api.get_me()

    assert_status_code(response, 401)
    data = response.json()
    assert data["msg"] == "Missing or invalid Authorization header"
