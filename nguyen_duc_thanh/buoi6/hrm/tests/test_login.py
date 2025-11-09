import os
import time

import json

from buoi6.hrm.components.header_component import HeaderComponent
from buoi6.hrm.components.sidebar_componen import SizeBarComponent
from buoi6.hrm.pages.login_page import LoginPage
def test_login_successfully(page):
    login_page = LoginPage(page)
    creds = login_page.get_credential()
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
    creds = login_page.get_credential()
    valid = creds["valid_user"]
    login_page.login(valid["username"], valid["password"])
    header_component = HeaderComponent(page)
    header_component.click_to_headers()


def test_login_invalid_password(page):
    login_page = LoginPage(page)
    creds = login_page.get_credential()
    valid = creds["invalid_user"]
    login_page.login(valid["username"], valid["password"])
    login_page.take_screenshot("test_login_invalid_password")
    login_page.assert_invalid_password()

