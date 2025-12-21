from playwright.sync_api import Page, expect
from pages.OrangeHRM.orange_hrm_page import OrangeHrmPage 
from core.base_page import BasePage 
from pages.OrangeHRM.hrm_dashboard_page import HRM_DashboardPage
from pages.OrangeHRM.Menu.profile_page import ProfilePage
import time

def test_upload_avatar_successfully(loggedinOrangePage):
    print("Go to Profile")
    profilepage = loggedinOrangePage.navigate_to_profile()
    user_name = profilepage.get_employee_fullname()
    print(f"User name: {user_name}")
    profilepage.update_avatar(f"./BT_Buoi9/data/googleicon.png")