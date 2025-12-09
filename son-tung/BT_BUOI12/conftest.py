import pytest
from playwright.sync_api import Playwright

@pytest.fixture(scope="session")
def browser(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False, channel="chrome")
    yield browser
    browser.close()

@pytest.fixture
def context(browser):
    context = browser.new_context(viewport={"width": 1400, "height": 900})
    yield context
    context.close()

@pytest.fixture
def page(context):
    page = context.new_page()
    yield page
    page.close()
