import pytest
from playwright.sync_api import Page
from Core.config import HRM_USERNAME, HRM_PASSWORD, ORG_PASSWORD ,ORG_USERNAME
from pages.HRM.login_page import LoginPage
from pages.Multitab_demo.OrangeLoginPage import OrangeLoginPage

@pytest.fixture (name="login_page")
def fixture_login_page(page:Page) ->LoginPage:
    return LoginPage(page)
# Trang HRM
@pytest.fixture(name="hrm_logged_in_page")
def fixture_hrm_logged_in_page(login_page:LoginPage) -> Page:
    login_page.open()
    login_page.login(HRM_USERNAME,HRM_PASSWORD)
    login_page.assert_login_success()
    return login_page.page
 
# Trang Orange
@pytest.fixture(name="orange_login_page")
def fixture_orange_login_page(page:Page) -> OrangeLoginPage:
    orange_page = OrangeLoginPage(page)
    orange_page.open()
    return orange_page

