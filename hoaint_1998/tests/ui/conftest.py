from pages.HRM.Login.login_page import LoginPage
import pytest
from utils.json_loader import load_json_file
import os


file_path_json_login_data = os.path.join(os.getcwd(), "data", "login_data", "credentials.json")

cred = load_json_file(file_path_json_login_data)
valid_user = cred["valid_user"]
base_url = "https://hrm.anhtester.com/erp"

@pytest.fixture
def login_page(page) -> LoginPage:
    return LoginPage(page)

@pytest.fixture
def logined_page(login_page) -> LoginPage:
    login_page.go_to_login_page(base_url)
    login_page.login(valid_user["username"], valid_user["password"])
    login_page.verify_login_success()
    return login_page