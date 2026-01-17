from pages.Book_API.login import Login


def assert_response_ok(res):
    assert res.ok, f"Request failed: {res.status} - {res.text()}"

def register(api_context_antester, new_user_data):
    payload = new_user_data
    res = api_context_antester.post("/api/register", data=payload)
    assert_response_ok(res)


def test_case_1(page, api_context_antester, new_user_data):
    register(api_context_antester, new_user_data)
    login = Login(page)
    login.open_login_page()
    login.login(new_user_data["email"], new_user_data["password"])
    
