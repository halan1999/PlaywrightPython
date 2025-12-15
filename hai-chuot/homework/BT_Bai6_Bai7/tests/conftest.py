import pytest
from playwright.sync_api import BrowserContext
from page.login_page import LoginPage
from page.home_page import HomePage
from utils.data_reader import DataReader

# ==================================================
# SCOPE CLASS
# Thực hiện với bộ test case (dạng Class) lấy dữ liệu từ file login_account.json
# Dữ liệu trả về sẽ danh sách valid và invalid user
# ==================================================
@pytest.fixture(scope="class")
def get_data_login(request):    

    user_data = DataReader.read_json_data("login_account.json")
    lst_valid = user_data["valid_user"]
    lst_invalid = user_data["invalid_user"]
    
    request.cls.lst_valid = lst_valid
    request.cls.lst_invalid = lst_invalid
    
    yield

# ==================================================
# SCOPE CLASS
# Thực hiện với bộ test case (dạng Class) phải thực hiện đăng nhập thành công trước khi thực thi toàn bộ test case trong Class
# Dữ liệu trả về sẽ là màn hình sau khi đăng nhập thành công --> Cụ thể là một đối tượng HomePage
# ==================================================
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

# ==================================================
# SCOPE FUNCTION
# Hàm sử dụng fixture (scope = module) để khởi tạo đối tượng Browser
# Thực hiện với function test được áp dụng
# SETUP: Mở trình duyệt và khởi tạo đối tượng LoginPage
# TEARDOWN: Đóng trình duyệt
# NOTE: Chỉ sử dụng khi bắt đầu thực thi test cần mở một trình duyệt mới
# ==================================================
@pytest.fixture(scope="function")
def initialize_test_script(open_browser):
    context = open_browser.new_context(viewport={"width": 1920, "height": 1080})

    login_page = create_login_page(context)

    yield login_page

    context.close()

# ==================================================
# NOTE: Đây không phải là fixture, chỉ là một hàm dùng để tái sử dụng
# Hàm thực hiện tạo đối tượng LoginPage sử dụng trong toàn bộ conftest.py
# ==================================================
def create_login_page(context : BrowserContext):
    URL = "https://hrm.anhtester.com/erp/login"
    page = context.new_page()

    login_page = LoginPage(page, URL)
    
    return login_page