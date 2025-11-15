import pytest

@pytest.mark.usefixtures("get_data_login")
class TestLoginPage:
    
    def test_login_pass(self, initialize_test_script):
        for user_info in self.lst_valid:
            username = user_info["username"]
            password = user_info["password"]
            
            initialize_test_script.login(username, password)
            initialize_test_script.verify_login_pass(username)

    def test_login_fail(self, initialize_test_script):
        for user_info in self.lst_invalid:
            username = user_info["username"]
            password = user_info["password"]
            
            initialize_test_script.login(username, password)
            initialize_test_script.verify_login_fail()