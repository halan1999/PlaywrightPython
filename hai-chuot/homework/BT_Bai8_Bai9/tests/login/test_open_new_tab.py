import pytest
from utils.data_reader import DataReader

def test_open_new_tab_and_login_logut(self, initialize_test_script):
        user_data = DataReader.read_json_data("login_account.json")  
        username = user_data["username"]
        password = user_data["password"]
        initialize_test_script.login(username, password)

        initialize_test_script._take_screenshot('login/login_successfully.png')
        initialize_test_script.verify_login_pass(username)   