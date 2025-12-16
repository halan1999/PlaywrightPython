
import pytest

from buoi7.pages.login_page import LoginPage

@pytest.fixture
def login_page(page):
    return LoginPage(page)

@pytest.fixture
def logged_page(login_page):
    creds = login_page.get_credential()
    login_page.login(creds["valid_user"]["username"], creds["valid_user"]["password"])
    return login_page
