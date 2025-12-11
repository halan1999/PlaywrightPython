import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="session")
def browser():
    """
    Fixture cho đối tượng Browser (Khởi tạo 1 lần/session).
    Sử dụng 'yield' để thực hiện Teardown sau khi tất cả các test kết thúc.
    """
    with sync_playwright() as p:
        # Setup: Khởi tạo trình duyệt Chromium (có thể thay bằng 'firefox' hoặc 'webkit')
        print("\n[SETUP] Khởi tạo Browser...")
        browser = p.chromium.launch(headless=False) # Dùng headless=False để xem giao diện
        yield browser # Trả về browser object cho các fixture khác

        # Teardown: Đóng trình duyệt sau khi tất cả test case hoàn thành
        print("\n[TEARDOWN] Đóng Browser...")
        browser.close()

@pytest.fixture(scope="function")
def page(browser):
    """
    Fixture cho đối tượng Page (Khởi tạo 1 lần/test function).
    Sử dụng 'yield' để thực hiện Teardown sau mỗi test function.
    """
    # Setup: Tạo Context và Page mới
    print("\n  [SETUP] Tạo Page mới...")
    context = browser.new_context()
    page = context.new_page()
    yield page # Trả về page object cho test function

    # Teardown: Đóng Page và Context sau khi test function kết thúc
    print("\n  [TEARDOWN] Đóng Page và Context...")
    page.close()
    context.close()