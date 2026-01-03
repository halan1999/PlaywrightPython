import pytest

def assert_json_response_ok(resp):
    assert resp.ok, f"request failed: {resp.status} - {resp.text}"
    assert resp.headers.get{"content-type",""}.startswith("application/json")

def test_get_posts(api_context, token):
    respond = api_context.get("/posts")
    assert respond.status == 200
    data = respond.json()
    assert isinstance(data,list)
    assert len(data) > 0

def test_delete_post(api_context):
    resp = api_context.delete("posts/1")
    assert resp.status ==200
    