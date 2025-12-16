import pytest
from page.login_page import LoginPage

@pytest.fixture(scope="function")
def initialize_test_script(open_browser):
    URL = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"

    context = open_browser.new_context(viewport={"width": 1920, "height": 1080})    
    page = context.new_page()
    
    login_page = LoginPage(page, URL)

    yield login_page

    context.close()