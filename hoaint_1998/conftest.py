from playwright.sync_api import Playwright, Browser, BrowserContext
import pytest
from pathlib import Path
import json

PROJECT_ROOT = Path(__file__).resolve().parent
DATA_FILE = PROJECT_ROOT / "data" / "credentials_parallel.json"

@pytest.fixture(scope="session")
def browser(playwright: Playwright):
    """
    khởi tạo browser, chùng chung chromium/firefox/webkit
    """
    browser = playwright.chromium.launch(headless=False, args=['--start-maximized'])
    yield browser
    browser.close()

@pytest.fixture(scope="function")
def context(browser: Browser):
    """
    Tạo session duyệt mới cho mỗi test (tránh ảnh hưởng test khác)
    """
    context = browser.new_context(no_viewport=True)
    yield context
    context.close()

@pytest.fixture(scope="function")
def page(context: BrowserContext):
    """
    Sinh tab mới cho mỗi test
    """
    page = context.new_page()
    # lấy screen size thật từ OS sau khi mở browser
    screen = page.evaluate("""
        () => ({
                width: window.screen.width,
                height: window.screen.height})
    """)
    page.set_viewport_size(screen)
    yield page
    page.close()

@pytest.fixture(scope="session")
def credentials():
    if not DATA_FILE.exists():
        raise FileNotFoundError(f"Credentials file not found at: {DATA_FILE}")
    return json.loads(DATA_FILE.read_text(encoding="utf-8"))

@pytest.fixture(scope="session")
def profiles(credentials):
    return list(credentials.key())

def pytest_generate_tests(metafunc):
    if "profile" in metafunc.fixturenames:
        creds =  metafunc.config._credentials_cache = (
            metafunc.config._credentials_cache
            if hasattr(metafunc.config, "_credentials_cache")
            else None
        )
        # load data only once
        if creds is None:
            creds = json.loads(DATA_FILE.read_text(encoding="utf-8"))
            metafunc.config._credentials_cache = creds
        profiles = list(creds.keys())[:3]
        metafunc.parametrize("profile", profiles, ids=profiles)