import pytest
from playwright.sync_api import sync_playwright

# 1. Lanch browser with headless = False
@pytest.fixture(scope='session')
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        yield browser
        browser.close()

# 2. Launch context (with clear cached - fresh broswer)
@pytest.fixture
def context(browser):
    context = browser.new_context(viewport={"width": 1400, "height": 900})
    yield context
    context.close()


# 3. Launch new page (page object)
@pytest.fixture
def page(context):
    page = context.new_page()
    yield page
    page.close()