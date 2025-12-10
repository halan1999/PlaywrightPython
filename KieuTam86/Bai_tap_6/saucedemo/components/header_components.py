from core.base_page import BasePage

class HeaderComponent(BasePage):
    """Đại diện cho thanh header hiển thị trên mọi trang."""

    Logo = ".app_logo"
    SHOPPING_CART_LINK = ".shopping_cart_link"
    MENU_BUTTON = "#react-burger-menu-btn"
    LOGOUT_LINK = "#logout_sidebar_link"

    def open_menu(self):
        """Mở menu điều hướng."""
        self._click(self.MENU_BUTTON)

    def logout(self):
        """Đăng xuất khỏi hệ thống."""
        self.open_menu()
        self._click(self.LOGOUT_LINK)

    def go_to_cart(self):
        """Chuyển sang trang giỏ hàng."""
        self._click(self.SHOPPING_CART_LINK)
                 
