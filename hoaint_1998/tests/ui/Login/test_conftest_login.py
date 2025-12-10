from components.header_components import HeaderComponents
from utils.json_loader import load_json_file
import os

file_path_json_login_data = os.path.join(os.getcwd(), "data", "login_data", "credentials.json")

cred = load_json_file(file_path_json_login_data)
valid_user = cred["valid_user"]
base_url = "https://hrm.anhtester.com/erp"

def test_conftest_login(login_page):
    login_page.go_to_login_page(base_url)
    login_page.login(valid_user["username"], valid_user["password"])
    login_page.verify_login_success()

def test_conftest_logined(logined_page, page):
    header = HeaderComponents(page)
    logined_page.run_header_flow()
    header._logout()