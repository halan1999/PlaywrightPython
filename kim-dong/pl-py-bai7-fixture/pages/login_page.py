from pages.base_page import BasePage
from playwright.sync_api import expect
from pages.secure_area_page import SecureAreaPage

class LoginPage(BasePage):
    """Đại diện cho trang đăng nhập của hệ thống."""

    # Locators (được định nghĩa như hằng số)
    URL = "https://the-internet.herokuapp.com/login"
    USERNAME_FIELD = "#username"
    PASSWORD_FIELD = "#password"
    LOGIN_BUTTON = ".radius"
    FLASH_MESSAGE = "#flash"

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
        # Trả về trang sau login (SecureAreaPage)
        return SecureAreaPage(self.page)

    @property
    def flash_message(self):
        return self.page.locator(self.FLASH_MESSAGE)