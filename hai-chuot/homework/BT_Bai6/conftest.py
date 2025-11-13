import pytest
from playwright.sync_api import Playwright


@pytest.fixture(scope="module")
def open_browser(playwright : Playwright):
    browser = playwright.chromium.launch(headless=False, channel="chrome")
    context = browser.new_context(viewport={"width": 1400, "height": 900})
    page = context.new_page()
    
    yield page

    page.close()
    context.close()
    browser.close()