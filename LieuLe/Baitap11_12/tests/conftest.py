# tests/conftest.py
import pytest
from playwright.sync_api import sync_playwright
from config.env import BASE_URL
from fixtures.auth_fixtures import *

@pytest.fixture(scope="session")
def playwright():
    with sync_playwright() as p:
        yield p

@pytest.fixture(scope="function")
def browser(playwright):
    browser = playwright.chromium.launch(headless=False)
    yield browser
    browser.close()

@pytest.fixture(scope="function")
def page(browser):
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()

@pytest.fixture(scope="session")
def api_request(playwright):
    request = playwright.request.new_context(
        base_url=BASE_URL
    )
    yield request
    request.dispose()
