import pytest
from playwright.sync_api import Playwright

# ================================
# 1. Browser – mở 1 lần cho cả session
# ================================
@pytest.fixture(scope="session")
def browser(playwright: Playwright):
    browser = playwright.chromium.launch(
        headless=False,
        channel="chrome",
        args=["--start-maximized"]
    )
    yield browser
    browser.close()
# ================================
#2. Create a fresh browser context for each test
# Không dính cookie test khác
# Không dính login test khác
# ================================
@pytest.fixture(scope="function")
def context(browser):
    context = browser.new_context()
    yield context
    context.close()
# ================================
#3. Create a new page object for each test
# ================================
@pytest.fixture(scope="function")
def page(context):
    page = context.new_page()
    yield page
    page.close()    