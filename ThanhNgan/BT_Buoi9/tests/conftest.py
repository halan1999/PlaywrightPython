import pytest
from playwright.sync_api import Page
from pages.orange_hrm_page import OrangeHrmPage


@pytest.fixture
def orangePage(page: Page):
    orangePage = OrangeHrmPage(page)
    orangePage.goto()
    return orangePage

@pytest.fixture
def loggedinOrangePage(orangePage):
    orangePage.login_with_valid_credentials()
    yield orangePage
