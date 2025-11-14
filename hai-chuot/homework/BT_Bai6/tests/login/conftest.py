import pytest
from page.login_page import LoginPage
from utils.data_reader import DataReader

@pytest.fixture(scope="class")
def get_data_login(request):
    URL = "https://hrm.anhtester.com/erp/login"

    user_data = DataReader.read_json_data("login_account.json")
    lst_valid = user_data["valid_user"]
    lst_invalid = user_data["invalid_user"]

    login_page = LoginPage(URL)
    
    request.cls.lst_valid = lst_valid
    request.cls.lst_invalid = lst_invalid
    request.cls.login_page = login_page
    yield