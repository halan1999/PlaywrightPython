import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture(scope="module")
def open_browser():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False, channel="chrome")
            
        yield browser

        browser.close()