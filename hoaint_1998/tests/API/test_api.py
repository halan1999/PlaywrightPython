import pytest
from playwright.sync_api import APIResponse


def assert_response_ok(res: APIResponse):
    assert res.ok, f"Request failed: {res.status} - {res.text()}"

@pytest.mark.skip
def test_get(api_context):
    res = api_context.get("post/1")

    assert res.ok, f""
    assert res.status == 200

    data = res.json()
    assert data["id"] == 1
    assert "title" in data

@pytest.mark.skip
def test_create(api_context):
    payload = {"title": "hoai", "body": "fish", "userId": 431998}
    res = api_context.post("/posts", data = payload)
    assert_response_ok(res)
    data = res.json()
    assert data["title"] == "hoai"
    assert data["body"] == "fish"
    assert data["userId"] == 431998
    assert "id" in data

@pytest.mark.skip
def test_put(api_context):
    payload = {"title": "Avatar", "body": "Pandora", "userId": 15432}
    res = api_context.put("/posts/1", data=payload)
    assert_response_ok(res)
    data = res.json()
    assert data["title"] == "Avatar"
    assert data["body"] == "Pandora"
    assert data["userId"] == 15432
    assert data["id"] == 1

@pytest.mark.skip
def test_patch(api_context):
    payload = {"title": "Avatar_01"}
    res = api_context.patch("/posts/1", data=payload)
    assert_response_ok(res)
    data = res.json()
    assert data["title"] == "Avatar_01"

# @pytest.mark.skip
def test_delete(api_context):
    res = api_context.delete("/posts/101")
    assert_response_ok(res)
