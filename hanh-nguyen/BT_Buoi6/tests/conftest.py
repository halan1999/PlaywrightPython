import pytest
from page.login_page import LoginPage

@pytest.fixture(scope="function")
def Login_page(page):
    return LoginPage()

@pytest.fixture(scope="function")
def Logged_in(Login_page):
    Login_page.open()
    cred = Login_page.read_credentials()
    Login_page.login(cred["valid_user"]["username"], cred["valid_user"]["password"])