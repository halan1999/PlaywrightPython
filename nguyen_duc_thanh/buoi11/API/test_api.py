from faker import Faker
fake = Faker()
def test_post_register(api_context):
    payload = {
        "name": fake.name(),
        "email": fake.email(),
        "password": "123456",
        "avatarUrl": "",
        "phone": fake.phone_number(),
        "address": fake.address()
    }
    res = api_context.post("/api/register", data=payload)
    assert res.status in (200, 201)
    data = res.json()
    assert data["msg"] == "Register successfully."

def test_post_login(api_context, register):
    payload = {
        "email": register["email"],
        "password": register["password"]
    }
    res = api_context.post("/api/login", data=payload)
    assert res.status == 200
    data = res.json()
    assert data["msg"] == "Login successfully."

def test_post_refetch(api_context):
    res = api_context.post("/api/refetch-token")
    assert res.status == 200
    data = res.json()
    assert data["msg"] == "Refetch token successfully."

def test_patch_profile(api_context,login):
    headers = {
        "Authorization": f"Bearer {login}"
    }
    payload = {
        "name": fake.name(),
    }
    res = api_context.patch("/api/profile", data=payload,headers=headers)
    assert res.status == 200
    # data = res.json()
    # assert data["msg"] == "success"

def test_get_me(api_context,login):
    headers = {
        "Authorization": f"Bearer {login}"
    }
    res = api_context.get("/api/profile",headers=headers)
    assert res.status == 200


def test_delete_logout(api_context,login):
    headers = {
        "Authorization": f"Bearer {login}"
    }
    res = api_context.delete("/api/logout",headers=headers)
    assert res.status == 200
    data = res.json()
    assert data["msg"] == "Logout successfully."
