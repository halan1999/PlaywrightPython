import pytest, allure

@allure.epic("HRM Anh tester")
@allure.feature("Account")
@allure.story("Login & Logout")
@pytest.mark.usefixtures("get_data_login")
class TestLoginPage:
    
    @allure.title("Login success")
    @allure.description("Verify user in test data login success")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_login_pass(self, initialize_test_script):
        for user_info in self.lst_valid:
            with allure.step("Get User in Test data"):
                username = user_info["username"]
                password = user_info["password"]
            
            with allure.step(f"Login with account : {username}"):
                initialize_test_script.login(username, password)

            with allure.step(f"Verify login success with {username}"):
                initialize_test_script.verify_login_pass(username)
                
            initialize_test_script._take_screenshot('login/login_successfully.png', "Đăng nhập thành công")

    @allure.title("Login Fail")
    @allure.description("Verify user in test data login failed")
    @allure.severity(allure.severity_level.NORMAL)
    def test_login_fail(self, initialize_test_script):
        for user_info in self.lst_invalid:
            with allure.step("Get User in Test data"):
                username = user_info["username"]
                password = user_info["password"]
            
            with allure.step(f"Login with account : {username}"):
                initialize_test_script.login(username, password)

            with allure.step(f"Verify login fail with {username}"):
                initialize_test_script.verify_login_fail()

            initialize_test_script._take_screenshot('login/login_failed.png', "Đăng nhập thất bại")
            print(initialize_test_script.get_message_error)

    @allure.title("Logout from header")
    @allure.description("Verify user logout from Header")
    @allure.severity(allure.severity_level.NORMAL)
    def test_logout_from_header(self, initialize_test_script):
        with allure.step("Get Valid User in Test data"):
            user_info = self.lst_valid[0]
            username = user_info["username"]
            password = user_info["password"]

        with allure.step(f"Login with account : {username}"):
                initialize_test_script.login(username, password)

        with allure.step(f"Verify login success with {username}"):        
            initialize_test_script.verify_login_pass(username)
        
        with allure.step("Logout from header"):
            initialize_test_script.logout_from_header()
        
        initialize_test_script._take_screenshot('logout/logout_from_header_successfully.png', "Đăng xuất thành công")

    @allure.title("Logout from button")
    @allure.description("Verify user logout from Button")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_logout_by_button(self, initialize_test_script):
        with allure.step("Get Valid User in Test data"):
            user_info = self.lst_valid[0]
            username = user_info["username"]
            password = user_info["password"]
            
        with allure.step("Get Valid User in Test data"):     
            initialize_test_script.login(username, password)
        
        with allure.step(f"Verify login success with {username}"): 
            initialize_test_script.verify_login_pass(username)
        
        with allure.step("Logout from button"):
            initialize_test_script.logout_by_button()

        initialize_test_script._take_screenshot('logout/logout_by_button_successfully.png', "Đăng xuất thành công")