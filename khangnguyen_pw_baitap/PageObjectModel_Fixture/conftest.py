import pytest
from pages.login_page import LoginPage

@pytest.fixture(scope="session")
def browser_context_args():
    return {
        "viewport": { "width": 1600, "height": 900}
    }

@pytest.fixture(scope="function")
def logged_in_page(page):


    login = LoginPage(page)
    login.open()
    login.login_valid()
    assert login.is_logged_in()
    return page
