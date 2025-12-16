import pytest
from playwright.sync_api import sync_playwright

# ==================================================
# MODULE SCOPE
# Executes once for each test_***.py file
# SETUP: Initialize non-headless Browser using Chromium-based Chrome
# TEARDOWN: Release the Browser object
# ==================================================
@pytest.fixture(scope="module")
def open_browser():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True, channel="chrome")
            
        yield browser

        browser.close()