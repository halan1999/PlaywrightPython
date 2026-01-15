import pytest
from playwright.sync_api import Playwright, Browser

#1. Launch browser (headless = False) => chạy cho toàn bộ TC mình muốn
@pytest.fixture(scope="session")
def browse(playwright: Playwright):
    #step setup
    browser = playwright.chromium.launch(headless=False)
    #return
    yield browser
    #Step Teardown
    browser.close()

#2. Create a fresh browser context for each test -> ko lưu lại cache - lịch sử cũ
@pytest.fixture
def context(browser):
    context = browser.new_context(viewport={"width": 1200, "height": 720})
    yield context
    context.close()

#3. Create a new page object for each test
@pytest.fixture
def page(context):
    page = context.new_page()
    yield page
    page.close()  