import pytest
from playwright.sync_api import Page
from page.login_page import LoginPage
from utils.data_reader import DataReader

@pytest.fixture(scope="class")
def get_data_login(request):
    

    user_data = DataReader.read_json_data("login_account.json")
    lst_valid = user_data["valid_user"]
    lst_invalid = user_data["invalid_user"]
    
    request.cls.lst_valid = lst_valid
    request.cls.lst_invalid = lst_invalid
    
    yield

@pytest.fixture(scope="function")
def initialize_test_script(open_browser):
    URL = "https://hrm.anhtester.com/erp/login"
    context = open_browser.new_context(viewport={"width": 1920, "height": 1080})
    page = context.new_page()

    login_page = LoginPage(page, URL)

    yield login_page

    page.close()
    context.close()