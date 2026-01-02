import pytest
from playwright.sync_api import Page
from pages.OrangeHRM.orange_hrm_page import OrangeHrmPage
from pages.OrangeHRM.hrm_dashboard_page import HRM_DashboardPage


@pytest.fixture
def orangePage(page: Page) -> OrangeHrmPage:
    orangePage = OrangeHrmPage(page)
    orangePage.goto()
    return orangePage

@pytest.fixture
def loggedinOrangePage(orangePage: OrangeHrmPage) -> HRM_DashboardPage:
    return orangePage.login_with_valid_credentials()

