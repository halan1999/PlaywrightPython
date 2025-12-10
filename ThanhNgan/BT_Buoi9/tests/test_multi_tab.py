from playwright.sync_api import Page, expect
from pages.orange_hrm_page import OrangeHrmPage 
from core.base_page import BasePage 
from pages.hrm_dashboard_page import HRM_DashboardPage
import time

def test_open_twitter_tab_successfully_then_login(orangePage):
    # Click icon Twitter to open new tab
    twitter_page = orangePage.open_social_tab("TWITTER_ICON")
    twitter_page._take_screenshot("orange_twitter_page")

    time.sleep(4)
    # Verify title 
    title = twitter_page.get_title_text()
    assert title == "OrangeHRM (@orangehrm) / X"
    
    time.sleep(2) 
    # Back to Orange HRM page
    orangePage._back_to_main_page()
    orangePage._take_screenshot("back_to_orange_hrm_page")

    # Login with valid credentials
    dashboard_page = orangePage.login_with_valid_credentials()
    print("Login successfully")

    # Verify title dashboard page
    dashboard_title = dashboard_page.get_title_text()
    assert dashboard_title == "OrangeHRM"

    # Logout
    dashboard_page.logout()
    print("Logout successfully")
