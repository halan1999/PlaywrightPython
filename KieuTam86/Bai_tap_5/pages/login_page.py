from pages.base_page import BasePage, expect
import time

class LoginPage(BasePage):
    #Save locator & action of Login page
    URL = "https://www.saucedemo.com/"
    Username_locator = "#user-name"
    Password_locator = "#password"
    Btn_Login = "#login-button"
    Error_h3 = "h3"
    Error_message_h3 = "Epic sadface: Sorry, this user has been locked out."

    def goto(self):
        self._open_page(self.URL)

    def login(self, username, password):
        self.goto()
        self._fill(self.Username_locator, username)
        self._fill(self.Password_locator, password)
        self._click(self.Btn_Login)
        time.sleep(5)
    def assert_error_message_visible(self):
        self._verify_text(self.Error_h3,self.Error_message_h3)
        print(self.Error_message_h3)




