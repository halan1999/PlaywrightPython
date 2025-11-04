from .base_page import BasePage
from playwright.sync_api import expect

class LoginPage(BasePage):

    URL = "https://www.saucedemo.com/"
    USERNAME_FIELD = "//input[@id='user-name']"
    PASSWORD_FIELD = "//input[@id='password']"
    LOGIN_BUTTON = "//input[@id='login-button']"
    ERROR_MESSAGE = "[data-test='error']"

    def goto(self):
        self._visit(self.URL)
    
    def login(self, username: str, password: str):
        self.goto()
        self._fill(self.USERNAME_FIELD, username, "Username Field")
        self._fill(self.PASSWORD_FIELD, password, "Password Field")
        self._click(self.LOGIN_BUTTON, "Login Button")
    
    def assert_login_successful(self):
        """Xác minh đăng nhập thành công."""
        expect(self.page).to_have_url("https://www.saucedemo.com/inventory.html")

    def assert_error_message_visible(self, expected_text):
        """Kiểm tra thông báo lỗi đăng nhập hiển thị đúng."""
        self._assert_text_visible(self.ERROR_MESSAGE, expected_text)