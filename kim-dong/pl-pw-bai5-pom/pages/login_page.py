from pages.base_page import BasePage
from playwright.sync_api import expect

class LoginPage(BasePage):
    """Đại diện cho trang đăng nhập của hệ thống."""

    # Locators (được định nghĩa như hằng số)
    URL = "https://www.saucedemo.com/"
    USERNAME_FIELD = "#user-name"
    PASSWORD_FIELD = "#password"
    LOGIN_BUTTON = "#login-button"
    ERROR_MESSAGE = "[data-test='error']"

    # Business Actions
    def goto(self):
        """Điều hướng tới trang Login."""
        self._visit(self.URL)

    def login(self, username, password):
        """Thực hiện nghiệp vụ đăng nhập."""
        self.goto()
        self._fill(self.USERNAME_FIELD, username, name="Username")
        self._fill(self.PASSWORD_FIELD, password, name="Password")
        self._click(self.LOGIN_BUTTON, name="Login Button")

    def assert_login_successful(self):
        """Xác minh đăng nhập thành công."""
        expect(self.page).to_have_url("https://www.saucedemo.com/inventory.html")

    def assert_error_message_visible(self, expected_text):
        """Kiểm tra thông báo lỗi đăng nhập hiển thị đúng."""
        self._assert_text_visible(self.ERROR_MESSAGE, expected_text)
