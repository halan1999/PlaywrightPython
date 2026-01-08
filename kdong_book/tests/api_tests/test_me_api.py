import allure
from models.user_model import RegisterPayload, RegisterResponse
from models.login_model import *
from models.me_model import *
from allure_commons.types import AttachmentType

@allure.epic("User Management")
@allure.feature("Register")
@allure.story("Register Success")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Test Register User - Success")
def test_me_api(api_context):
    with allure.step("Prepare register payload"):
        payload_obj = RegisterPayload()
        payload_dict = payload_obj.to_dict()
        allure.attach(str(payload_dict), name="Request Payload", attachment_type=allure.attachment_type.JSON)
    
    with allure.step(f"Register new account"):
        response = api_context.post("/api/register", data=payload_dict)
        allure.attach(response.text(), name="Response Body", attachment_type=allure.attachment_type.JSON)
        allure.attach(
            body=f"Response Status: {response.status}",
            name="Response Status",
            attachment_type=AttachmentType.TEXT
        )
    with allure.step(f"Send POST request to /api/login"):
        login_response = api_context.post("/api/login", data=payload_dict)
        assert login_response.ok, f"Login không thành công! Status: {login_response.status}"

        print (login_response)
    with allure.step(f"Send GET request to /api/me"):
        token = login_response.json().get("accessToken")
        response = api_context.get(
            "/api/me",
            headers={"authorization": f"Bearer {token}"}
        )   
    assert response.status == 200
    res = LoginResponse(response.json())
    print(response.json())

    actual_data = response.json()
    me = MeResponse(actual_data)

    assert me.id is not None, "ID should not be null"
    assert isinstance(me.id, str), "ID should be a string"