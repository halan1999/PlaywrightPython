import pytest, requests
from playwright.sync_api import Playwright

def assert_json_response_ok(resp):
    assert resp.ok, f"Request failed: {resp.status} - {resp.text()}"
    #Can check BE response wrong content-type
    assert resp.headers.get("content-type", "").startswith("application/json"), \
        f"Unexpected content-type: {resp.headers.get('content-type')}"

def test_get_posts_1(api_context_typicode):
    resp = api_context_typicode.get("/posts/1")
    assert_json_response_ok(resp)
    assert resp.status == 200
    data = resp.json()
    assert data["id"] == 1
    assert data["title"] == "sunt aut facere repellat provident occaecati excepturi optio reprehenderit"
    assert data["body"] == "quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto"
    print("Get API posts/1 successfully")

def test_get_posts_2(api_context_typicode):
    responds = api_context_typicode.get("posts/2")
    assert_json_response_ok(responds)
    assert responds.status == 200
    data = responds.json()
    assert data["id"] == 2
    assert data["title"] == "qui est esse"
    assert data["body"] == "est rerum tempore vitae\nsequi sint nihil reprehenderit dolor beatae ea dolores neque\nfugiat blanditiis voluptate porro vel nihil molestiae ut reiciendis\nqui aperiam non debitis possimus qui neque nisi nulla"
    print("Get API posts/2 successfully")

def test_get_posts(api_context_typicode):
    responds = api_context_typicode.get("/posts")
    assert_json_response_ok(responds)
    assert responds.status == 200
    # Parse response
    data = responds.json()
    assert isinstance(data, list), "Response is not a list"

    print(f"Total posts={len(data)}")
    for post in data:
        print(f"User ID: {post['userId']} | "
            f"Post ID: {post['id']} | "
            f"Title: {post['title']} | "
            f"Body: {post['body']} \n"
        )

def test_create_post(api_context_typicode):
    payload = {"title": "playwright python", "body": "hello world", "userId": 1}
    respond = api_context_typicode.post("/posts", data=payload)
    assert_json_response_ok(respond)
    created = respond.json()
    # JSONPlaceholder thường trả is = 001
    assert created["title"] == "playwright python"
    assert created["body"] == "hello world"
    assert created["userId"] == 1
    assert "id" in created

# def test_get_user(api_context):
#     resp = api_context.get("/api/user")
