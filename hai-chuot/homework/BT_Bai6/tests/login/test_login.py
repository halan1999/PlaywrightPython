import pytest

@pytest.mark.usefixtures("get_data_login")
class TestLoginPage:
    
    def test_login_pass(self):
        for user_info in self.lst_valid:
            username = user_info["username"]
            password = user_info["password"]
            
            self.login_page.login(username, password)
            self.login_page.verify_login_pass(username)