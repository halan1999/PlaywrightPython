from pages.base_page import BasePage

class LoginPage(BasePage):
    URL = "https://www.saucedemo.com/"
    Xpath_ipt_username = '//input[@id="user-name"]'
    Xpath_ipt_password = '//input[@id="password"]'
    Xpath_btn_login = '//input[@id="login-button"]'
    
    def login(self, username : str, password : str):
        self._goToURL(self.URL)
        self._setText(self.Xpath_ipt_username, username)
        self._setText(self.Xpath_ipt_password, password)
        self._click(self.Xpath_btn_login)

    def assert_login_pass(self):
        super()._verify_home_page_visible()