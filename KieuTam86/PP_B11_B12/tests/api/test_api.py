import pytest, requests
# from playwright.sync_api import Playwright
# import allure


def assert_json_response_ok(resp):
    assert resp.ok, f"Request failed: {resp.status} - {resp.text()}"
    #Can check BE response wrong content-type
    assert resp.headers.get("Content-Type", "").startswith("application/json"), \
        f"Unexpected content-type: {resp.headers.get('Content-Type')}"

def test_register_api(api_context, new_user_data):
    payload = new_user_data
    responds_user_register = api_context.post("api/register",data=payload)
    
    assert responds_user_register.status in [200, 201]
    assert responds_user_register.status_text == "Created"
    body = responds_user_register.json()
    assert "msg" in body
    assert body["msg"] == "Register successfully."

def test_login_with_register_user(api_context, registered_user):
    respond_user_login = api_context.post("/api/login",data={
        "email": registered_user["email"],
        "password": registered_user["password"]
    })   
    assert respond_user_login.status == 200
    body = respond_user_login.json()
    assert "accessToken" in body
    assert body["accessToken"] is not None
    assert body["msg"] == "Login successfully."
    # assert respond_user_login["exp"] == "6d"
    print("Login succesfully!")

def test_refetch_token_api(api_context, auth_token):
    resp = api_context.post('api/refetch-token',
        headers={"Authorization": f"Bearer {auth_token}"}
    )
    assert resp.status == 200
    body = resp.json()
    assert "accessToken" in body
    assert body["msg"] == "Refetch token successfully."
    token_refetch = body["accessToken"]
    print(f"Token: {token_refetch}")

def test_get_me_api(api_context, auth_token, registered_user):
    resp = api_context.get("/api/me",
        headers={"Authorization": f"Bearer {auth_token}"}
    )
    assert resp.status == 200
    body = resp.json()
    assert body["name"] == registered_user["name"]
    assert body["email"] == registered_user["email"]
    assert body["avatarUrl"] == registered_user["avatarUrl"]
    assert body["phone"] == registered_user["phone"]
    assert body["address"] == registered_user["address"]
    print("Print infomation of me:")
    print(body)

def test_patch_profile_api(api_context, auth_token, registered_user):
    resp = api_context.patch("/api/profile",
        headers={"Authorization": f"Bearer {auth_token}"},
        data={"name": "Tam QA", "email": registered_user["email"]}
    )
    assert resp.status == 200
    body = resp.json()
    assert body["msg"] == "Updated profile successfully."
    print("Updated profile successfully.")

def test_logout_api(api_context, auth_token):
    resp = api_context.delete("api/logout",
        headers={"Authorization": f"Bearer {auth_token}"}
    )
    assert resp.status == 200
    body = resp.json()
    assert body["msg"] == "Logout successfully."
    print("Logout successfully.")

