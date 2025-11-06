from playwright.sync_api import expect, Page
import pytest
from pages.login_hrm_page import LoginHrmPage
from components.header_component import HeaderComponent

@pytest.fixture(scope="function")
def login_success(page) -> None:
    login_page = LoginHrmPage(page)
    # Step 1: Visit login page
    login_page.visit_login_page()
    # Step 2: Perform login action
    login_page.login("admin_example", "123456")
    # Step 3: Verify successful login by checking URL
    expect(page).to_have_url("https://hrm.anhtester.com/erp/desk")
    print("Login test passed successfully")
    return page

def test_Header_account_setting(login_success: Page):
    page = login_success
    header = HeaderComponent(page)
    #  Open and capture Evd Account_setting
    header.open_account_setting()
    print("Mở Account setting thành công")

def test_Header_app(login_success: Page):
    page = login_success
    header = HeaderComponent(page)
    #  Open and capture Evd Apps
    header.open_apps()
    print("Mở App thành công")

def test_Header_calendar(login_success: Page):
    page = login_success
    header = HeaderComponent(page)
    #  Open and capture Evd System Calendar
    header.open_calendar()
    print("Mở System Calendar thành công")

def test_Header_report(login_success: Page):
    page = login_success
    header = HeaderComponent(page)
    #  Open and capture Evd System Report
    header.open_system_report()
    print("Mở System Report thành công")

def test_Header_language(login_success: Page):
    page = login_success
    header = HeaderComponent(page)
    #  Open and capture Evd System Report
    header.open_language()
    print("Mở language thành công")

def test_Header_todolist(login_success: Page):
    page = login_success
    header = HeaderComponent(page)
    #  Open and capture Evd System Report
    header.open_todolist()
    print("Mở todolist thành công")

def test_Header_logout(login_success: Page):
    page = login_success
    header = HeaderComponent(page)
    #  Open and capture Evd System Report
    header.click_user()
    header.click_logout()
    print("logout thành công")

    

    
