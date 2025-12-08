import pytest
from pages.HRM.login_page import LoginPage

@pytest.fixture
def hrm_login_page(page):
    return LoginPage(page)
@pytest.fixture
def hrm_logged_in(hrm_login_page):
    hrm_login_page.open()
    hrm_login_page.login("admin_example", "123456")
    hrm_login_page.assert_login_success()
    return hrm_login_page.page
# Trang Orange
import pytest
from playwright.sync_api import Page
from pages.Multitab_demo.OrangeLoginPage import OrangeLoginPage
@pytest.fixture
def orange_login_page(page:Page) -> OrangeLoginPage:
    orange_page = OrangeLoginPage(page)
    orange_page.open()
    return orange_page

