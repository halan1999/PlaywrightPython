import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="session")
def api_context ():
    with sync_playwright() as p:
        request_context = p.request.new_context(
            base_url="https://jsonplaceholder.typicode.com",
            extra_http_headers={
                "Accept" : "application/json"
            }
        )
        yield request_context
        request_context.dispose()
    


# def register_user(api_context, payload: dict):

#     res = api_context.post("/api/register", data=payload)

#     # print(res.headers)

#     if res.ok:

#         return res.json()

 

#     res2 = api_context.post("/api/register", data={"fields": payload})

#     # print(res.extra_http_headers)

#     if res2.ok:

#         print(res.json())

#         return res2.json()

 

#     raise AssertionError(

#         f"Register failed.\n"

#         f"Try1: {res.status} - {res.text()}\n"

#         f"Try2: {res2.status} - {res2.text()}"

#     )