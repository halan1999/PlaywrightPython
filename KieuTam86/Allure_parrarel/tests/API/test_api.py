import pytest

def assert_json_response_ok(resp):
    assert resp.ok, f"Request failed: {resp.status} - {resp.text()}"
    #Can check BE response wrong content-type
    assert resp.headers.get("content-type", "").startswith("application/json"), \
        f"Unexpected content-type: {resp.headers.get('content-type')}"

def test_get_posts(api_context):
    resp = api_context.get("/posts/1")
    assert_json_response_ok(resp)
    assert resp.status == 200
    data = resp.json()
    assert data["id"] == 1
    assert data["title"] == "sunt aut facere repellat provident occaecati excepturi optio reprehenderit"
    assert data["body"] == "quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto"
    print("Get API posts/1 successfully")

# def test_create_post(api_context):
#     payload = {"title": "play", "body": "world", "userId": 1}
#     resp = api_context.post("/posts", data=payload)
#     assert_json_response_ok(resp)
#     created = resp.json()
#     # JSONPlaceholder return id=101
#     assert created["title"] == "hello"
#     assert created["body"] == "world"
#     assert created["userId"] == 1
#     assert "id" in created