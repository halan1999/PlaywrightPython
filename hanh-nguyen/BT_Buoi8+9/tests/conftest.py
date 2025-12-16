import pytest
from playwright.sync_api import Page
from pages.login_page import LoginPage


@pytest.fixture
def HRMLoginPage(page: Page):
    HRMLoginPage = LoginPage(page)
    HRMLoginPage.goto()
    return HRMLoginPage

@pytest.fixture
def loggedinHRM(HRMLoginPage):
    HRMLoginPage.login_with_valid_credentials()
    yield HRMLoginPage