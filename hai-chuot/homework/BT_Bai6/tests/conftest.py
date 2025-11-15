import pytest
from playwright.sync_api import BrowserContext
from page.login_page import LoginPage
from page.home_page import HomePage
from utils.data_reader import DataReader

@pytest.fixture(scope="class")
def get_data_login(request):    

    user_data = DataReader.read_json_data("login_account.json")
    lst_valid = user_data["valid_user"]
    lst_invalid = user_data["invalid_user"]
    
    request.cls.lst_valid = lst_valid
    request.cls.lst_invalid = lst_invalid
    
    yield

@pytest.fixture(scope="class")
def login_pass_page(request, open_browser): 
    context = open_browser.new_context(viewport={"width": 1920, "height": 1080})
    user_data = DataReader.read_json_data("login_account.json")
    lst_valid = user_data["valid_user"]

    user_info = lst_valid[0]
    username = user_info["username"]
    password = user_info["password"]

    login_page = create_login_page(context)
    
    login_page.login(username, password)
    login_page.verify_login_pass(username)

    home_page = HomePage(login_page.get_page)

    request.cls.home_page = home_page
    
    yield

@pytest.fixture(scope="function")
def initialize_test_script(open_browser):
    URL = "https://hrm.anhtester.com/erp/login"
    context = open_browser.new_context(viewport={"width": 1920, "height": 1080})
    page = context.new_page()

    login_page = create_login_page(context)

    yield login_page

    page.close()
    context.close()

def create_login_page(context : BrowserContext):
    URL = "https://hrm.anhtester.com/erp/login"
    page = context.new_page()

    login_page = LoginPage(page, URL)
    
    return login_page