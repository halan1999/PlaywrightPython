import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="function")
def initial_context(initial_playwright):
    request_context = initial_playwright.request.new_context(
        base_url="https://book.anhtester.com",
        extra_http_headers= {
            "Content-Type": "application/json"
        }
    )

    yield request_context
    request_context.storage_state(path="auth.json")
    request_context.dispose()

@pytest.fixture(scope="function")
def initial_page(initial_playwright):
    browser = initial_playwright.chromium.launch(headless=False)
    context = browser.new_context(viewport={"width": 1920, "height": 1080})
    page = context.new_page()
    yield page
    page.close()
    context.close()
    browser.close()

@pytest.fixture(scope="function")
def initial_page_with_storage_state(initial_playwright):
    browser = initial_playwright.chromium.launch(headless=False)
    context = browser.new_context(viewport={"width": 1920, "height": 1080}, storage_state="auth.json")
    page = context.new_page()
    yield page
    page.close()
    context.close()
    browser.close()