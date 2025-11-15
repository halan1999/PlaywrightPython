from playwright.sync_api import Playwright, Browser, BrowserContext
import pytest

@pytest.fixture(scope="session")
def browser(playwright: Playwright):
    """
    khởi tạo browser, chùng chung chromium/firefox/webkit
    """
    browser = playwright.chromium.launch(headless=False, args=['--start-maximized'])
    yield browser
    browser.close()

@pytest.fixture(scope="function")
def context(browser: Browser):
    """
    Tạo session duyệt mới cho mỗi test (tránh ảnh hưởng test khác)
    """
    context = browser.new_context(no_viewport=True)
    yield context
    context.close()

@pytest.fixture(scope="function")
def page(context: BrowserContext):
    """
    Sinh tab mới cho mỗi test
    """
    page = context.new_page()
    # lấy screen size thật từ OS sau khi mở browser
    screen = page.evaluate("""
        () => ({
                width: window.screen.width,
                height: window.screen.height})
    """)
    page.set_viewport_size(screen)
    yield page
    page.close()