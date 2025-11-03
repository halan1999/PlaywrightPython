from pages.base_page import BasePage

class LoginPage(BasePage):
    Xpath_ipt_username = '//input[@id="user-name"]'
    Xpath_ipt_password = '//input[@id="password"]'
    Xpath_btn_login = '//input[@id="login-button"]'
    
    def login(self, username : str, password : str):
        self.page.locator(self.Xpath_ipt_username).fill(username)
        self.page.locator(self.Xpath_ipt_password).fill(password)
        self.page.locator(self.Xpath_btn_login).click()

    def assert_login_pass(self):
        super()._verify_home_page_visible()