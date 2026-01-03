import pytest
from playwright.sync_api import Playwright

# 1. Launch browser (headless=False)

@pytest.fixture(scope="session")
def brower(playwright:Playwright):
    brower=playwright.chromium.launch(headless=False)
    yield brower
    brower.close()

# 2. Create a fresh browser context for each test
@pytest.fixture
def context(brower):
    context=brower.new_context(viewport={"width":1400,"height":900})
    yield context
    context.close()

# 3. Create a new page object for each test
@pytest.fixture
def page(context):
    page=context.new_page()
    yield page
    page.close()
    