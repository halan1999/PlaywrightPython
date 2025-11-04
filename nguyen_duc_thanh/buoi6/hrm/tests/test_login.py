import os
import time
from buoi5.hrm.components.header_component import HeaderComponent
from buoi5.hrm.components.sidebar_componen import SizeBarComponent
from pages.login_page import LoginPage
import json
def test_login_successfully(page):
    login_page = LoginPage(page)
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, "../data/credentials.json")
    with open(file_path) as f:
        creds = json.load(f)
    valid = creds["valid_user"]
    login_page.login(valid["username"], valid["password"])
    login_page.assert_login_successful()
    login_page.take_screenshot("test_login_successfully.png")
    time.sleep(3)
    sizebar_component = SizeBarComponent(page)
    sizebar_component.scroll_to_end()
    login_page.take_screenshot("scroll_to_end_sizebar.png")

def test_logout_successfully(page):
    login_page = LoginPage(page)
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, "../data/credentials.json")
    with open(file_path) as f:
        creds = json.load(f)
    valid = creds["valid_user"]
    login_page.login(valid["username"], valid["password"])
    header_component = HeaderComponent(page)
    header_component.click_to_logout()
    login_page.take_screenshot("test_logout_successfully.png")

def test_click_header_component(page):
    login_page = LoginPage(page)
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, "../data/credentials.json")
    with open(file_path) as f:
        creds = json.load(f)
    valid = creds["valid_user"]
    login_page.login(valid["username"], valid["password"])
    header_component = HeaderComponent(page)

    #Click to Account Setting
    header_component.click_to_account_setting()
    time.sleep(3)
    login_page.take_screenshot("click_to_account_setting.png")

    #Click to Apps 
    header_component.click_to_apps()
    time.sleep(3)
    login_page.take_screenshot("click_to_apps.png")

    #Click to System Calender
    header_component.click_to_system_calender()
    time.sleep(3)
    login_page.take_screenshot("click_to_system_calender.png")

    #Click to System Report
    header_component.click_to_system_report()
    time.sleep(3)
    login_page.take_screenshot("click_to_system_report.png")

    #Click to Flag Languague
    header_component.click_to_languague()
    time.sleep(3)
    login_page.take_screenshot("click_to_languague.png")

# def test_login_failure(page):
#     login_page = LoginPage(page)
#     login_page.login("admin_example", "1234567")
#     login_page.assert_login_failed()

# def test_forgot_password(page):
#     login_page = LoginPage(page)
#     login_page.goto_forgot_password()
#     login_page.assert_goto_forgot_password()