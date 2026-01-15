import pytest

def assert_json_response_ok(resp):
    assert resp.ok, f"request failed: {resp.status} - {resp.text}"
    assert resp.headers.get("content-type","").startswith("application/json")

def test_get_posts(api_context):
    respond = api_context.get("/posts/1")
    assert respond.status == 200
    data = respond.json()
    assert data["id"] == 1
    assert data["title"] == "sunt aut facere repellat provident occaecati excepturi optio reprehenderit"
    assert data["body"] == "quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto"

def test_create_post(api_context):
    payload = {"title": "new topic", "body":"hello playwright with python", "userId":1}
    respond = api_context.post("/posts", data = payload)
    assert_json_response_ok(respond)
    created = respond.json()
    assert created["title"] == "new topic"
    assert created["body"] == "hello playwright with python"
    assert created["userId"] == 1
    assert "id" in created

# def test_delete_post(api_context):
#     resp = api_context.delete("posts/1")
#     assert resp.status == 200
#     data = resp.json()
#     assert data["id"] == 1
#     assert data["title"] == "sunt aut facere repellat provident occaecati excepturi optio reprehenderit"
#     assert data["body"] == "quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto"

    