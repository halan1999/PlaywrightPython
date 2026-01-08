import allure
from models.user_model import RegisterPayload, RegisterResponse
from models.login_model import *
from allure_commons.types import AttachmentType

@allure.epic("User Management")
@allure.feature("Register")
@allure.story("Register Success")
@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Test Register User - Success")
def test_login_api(api_context):
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
        response = api_context.post("/api/login", data=payload_dict)
        allure.attach(response.text(), name="Response Body", attachment_type=allure.attachment_type.JSON)
        allure.attach(
            body=f"Response Status: {response.status}",
            name="Response Status",
            attachment_type=AttachmentType.TEXT
        )
    print(f"\nDEBUG PAYLOAD: {payload_dict}")
    with allure.step("Verify status code and message"):
        
        assert response.status == 200
        res = LoginResponse(response.json())
        print(response.json())
        assert res.message == "Login successfully.", f"Lỗi message: {res.message}"
