import pytest

@pytest.mark.usefixtures("get_data_login")
class TestLoginPage:
    
    def test_login_pass(self, initialize_test_script):
        for user_info in self.lst_valid:
            username = user_info["username"]
            password = user_info["password"]
            
            initialize_test_script.login(username, password)
            initialize_test_script.verify_login_pass(username)
            initialize_test_script._take_screenshot('login/login_successfully.png')

    def test_login_fail(self, initialize_test_script):
        for user_info in self.lst_invalid:
            username = user_info["username"]
            password = user_info["password"]
            
            initialize_test_script.login(username, password)
            initialize_test_script.verify_login_fail()
            initialize_test_script._take_screenshot('login/login_failed.png')
            print(initialize_test_script.get_message_error)

    def test_logout_from_header(self, initialize_test_script):
        user_info = self.lst_valid[0]
        username = user_info["username"]
        password = user_info["password"]
            
        initialize_test_script.login(username, password)
        initialize_test_script.verify_login_pass(username)
        
        initialize_test_script.logout_from_header()
        initialize_test_script._take_screenshot('logout/logout_from_header_successfully.png')

    def test_logout_by_button(self, initialize_test_script):
        user_info = self.lst_valid[0]
        username = user_info["username"]
        password = user_info["password"]
            
        initialize_test_script.login(username, password)
        initialize_test_script.verify_login_pass(username)
        
        initialize_test_script.logout_by_button()
        initialize_test_script._take_screenshot('logout/logout_by_button_successfully.png')