import pytest, json, random, string, time
from playwright.sync_api import Playwright

@pytest.fixture(scope="session")
def api_context_typicode(playwright: Playwright):
    request_context = p.request.new_context(
        base_url="https://jsonplaceholder.typicode.com",
        extra_http_headers={
            "Accept": "application/json"
            }
        )
    yield request_context
    request_context.dispose()

@pytest.fixture(scope="session")
def api_context(playwright: Playwright):
    request_context = playwright.request.new_context(
        base_url ="https://book.anhtester.com",
        extra_http_headers={
            "Accept":"application/json",
            "Content-Type": "application/json",
        }    
    )
    yield request_context
    #Purpose : clear cache, memory after using
    request_context.dispose()

def random_email():
    suffix = "".join(random.choices(string.ascii_lowercase + string.digits, k=8))
    # num = int(time.time())
    return f"kieutam_{suffix}@mailqa.com"

def random_password():
    return "abc@ABC123" #demo; 

@pytest.fixture
def new_user_data():
    return {
        "email": random_email(),
        "name": "KieuTam",
        "password": random_password(),
        "phone": "0981110001",
        "address": "HCM",
        "avatarUrl": ""
    }

@pytest.fixture
def registered_user(api_context, new_user_data):
    resp = api_context.post("api/register",data=new_user_data)
    assert resp.status in [200, 201]
    return new_user_data

@pytest.fixture
def auth_token(api_context, registered_user):
    resp = api_context.post("/api/login", data={
        "email": registered_user["email"],
        "password": registered_user["password"]
    })
    assert resp.status == 200
    body = resp.json()
    assert "accessToken" in body
    return  body["accessToken"]

# config for web application fixture: brownser, context, new page
@pytest.fixture(scope="session")
def browser(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    yield browser
    browser.close()

@pytest.fixture(scope="function")
def page(browser):
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()




