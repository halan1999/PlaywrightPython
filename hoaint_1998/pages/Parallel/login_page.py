from core.base_page import BasePage

class LoginPage(BasePage):
    URL = "https://www.saucedemo.com/"
    username_input = "//input[@id='user-name']"
    password_input = "//input[@id='password']"
    login_button = "//input[@id='login-button']"


    def __init__(self, page):
        super().__init__(page)

    def open(self):
        self._goto(self.URL)

    def login(self, username, password):
        self._fill(self.username_input, username)
        self._fill(self.password_input, password)
        self._click(self.login_button)

    
