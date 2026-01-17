import pytest, json
from playwright.sync_api import Playwright
from pages.orange_hrm_page import Oranage_HRM
from pages.dash_board import Dashboard
from playwright.sync_api import sync_playwright

# PROJECT_ROOT = Path(__file__).resolve().parent
# DATA_FILE = PROJECT_ROOT / "data" / "credential_parallel.json"

#1. Page Object: Login Page
@pytest.fixture
def orange_page(page):
    return Oranage_HRM(page)

#2. Fixture thực hiện login (optional nếu cần login sẵn)
@pytest.fixture
def logged_in_page(page):
    orm = Oranage_HRM(page)
    orm.login_valid_user()

    return page


# @pytest.fixture
# def dashboard_page(page):
#     login = Oranage_HRM()

#     login.goto()
#     login.login_valid_user()

    # dashboard = Dashboard()
    # dashboard.assert_is_current_page()


#3. Class scope
# @pytest.fixture(scope="class")
# def logged_in_class(request, browser):
#     context = browser.new_context()
#     page = context.new_page()

#     #Login 1 lần cho cả class
#     lp = LoginPage(page)
#     lp.open()
#     lp.login()
#     lp.header.wait_for_user_logged_in()

@pytest.fixture(scope="session")
def credentials():
    if not DATA_FILE.exist():
        raise FileNotFoundError(
            f"Credentials file not found at: {DATA_FILE}"
        )
    return json.load(DATA_FILE.read_text(encoding="utf-8"))

@pytest.fixture(scope="session")
def profiles(credentials):
    return list(credentials.key())

def pytest_generate_tests(metafunc):
    if "profile" in metafunc.fixturenames:
        creds = metafunc.config._credentials_cache = (
            metafunc.config._credentials_cache
            if hasattr(metafunc.config, "_credentials_cache")
            else None
        )
        #load data only once
        if creds is None:
            creds = json.loads(DATA_FILE.read_text(enconding="utf-8"))
            metafunc.config._credentials_cache = creds

        profiles = list(creds.keys())[:6]
        metafunc.parametrize("profile", profiles, ids=profiles)

@pytest.fixture(scope="session")
def api_context():
    with sync_playwright() as p:
        request_context = p.request.new_context(
            base_url="https://jsonplaceholder.typicode.com",
            extra_http_headers={
                "Accept": "application/json"
            }
        )
        # return object
        yield request_context
        request_context.dispose()

# @pytest.fixture(scope="session")
# def api_anhtester_context():
#     with sync_playwright() as p:
#         request_context = p.request.new_context(
#             base_url ="https://jsonplaceholder.typicode.com",
#             extra_http_headers={
#             "Accept": "application/json"
#             }    
#         )
#         yield request_context
#         request_context.dispose()

