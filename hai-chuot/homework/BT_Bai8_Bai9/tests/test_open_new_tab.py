from utils.data_reader import DataReader
from page.login_page import LinkFooter
from page.x_page import XPage

def test_open_new_tab_and_login_logut(initialize_test_script):
        # Setup test data
        user_data = DataReader.read_json_data("login_account.json")  
        username = user_data["username"]
        password = user_data["password"]
        expected_header_title = 'Dashboard'

        # Navigate X page by icon
        x_page = XPage(initialize_test_script.open_related_page(LinkFooter.TWITTER))
        x_page.verify_x_icon()
        x_page.verify_title()
        x_page._take_screenshot('X_page.png') 

        # Login Orange HRM
        initialize_test_script.back_to_login_page()
        initialize_test_script.login(username, password)
        initialize_test_script.verify_login_success(expected_header_title)
        initialize_test_script._take_screenshot('login_successfully.png')

        # Logout Orange HRM
        initialize_test_script.logout()
        initialize_test_script._take_screenshot('logout_successfully.png')