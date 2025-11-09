import pytest
from playwright.sync_api import Playwright


# 1. Launch browser (headless = False)
@pytest.fixture(scope="session")
def browser(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False, channel="chrome")
    yield browser
    browser.close()


# 2. Create a fresh browser context for each test
@pytest.fixture
def context(browser):
    context = browser.new_context(viewport={"width": 1400, "height": 900})
    yield context
    context.close()


# 3. Create a new page object for each test
@pytest.fixture
def page(context):
    page = context.new_page()
    yield page
    page.close()

