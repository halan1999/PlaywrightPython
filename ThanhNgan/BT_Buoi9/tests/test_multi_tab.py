from playwright.sync_api import Page, expect
from pages.OrangeHRM.orange_hrm_page import OrangeHrmPage 
from core.base_page import BasePage 
from pages.OrangeHRM.hrm_dashboard_page import HRM_DashboardPage
import time

def test_open_twitter_tab_successfully_then_login(orangePage):
    print("Goto twitter page")
    # Click icon Twitter to open new tab
    twitter_page = orangePage.open_twitter_tab()
    
    
    # Verify title & icon
    assert twitter_page._get_url() == twitter_page.URL
    twitter_page.expect_icon_visible()
    assert twitter_page.get_text_under_avatar() == "OrangeHRM"
    twitter_page._take_screenshot("2.open_orange_twitter_page")

    # time.sleep(2) 
    # Back to Orange HRM page
    orangePage._back_to_main_page()
    orangePage._take_screenshot("3.back_to_orange_hrm_page")

    # Login with valid credentials
    dashboard_page = orangePage.login_with_valid_credentials()
    dashboard_page._take_screenshot("4.after_login_orange_hrm_page")
    print("Login successfully")

    # Verify title dashboard page
    dashboard_title = dashboard_page.get_title_text()
    assert dashboard_title == "OrangeHRM"

    # Logout
    dashboard_page.logout()
    dashboard_page._take_screenshot("5.after_logout")
    print("Logout successfully")
