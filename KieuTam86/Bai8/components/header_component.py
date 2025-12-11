from core.base_page import BasePage

class HeaderComponent(BasePage):
    """Đại diện cho thanh header hiển thị trên mọi trang."""

    header_items = [
        "//header//a[@data-original-title='Account Settings']",
        "//header//span[@data-original-title='Apps']",
        "//header//a[@data-original-title='System Calendar']",
        "//header//a[@data-original-title='System Reports']",
        "//header//li[1]//a[@data-toggle='dropdown']",
        "//header//a[@data-original-title='Todo List']"
    ]    
    btn_logout = "//a[@class='btn btn-smb btn-outline-primary rounded-pill']"
    profile_icon = "//img[@class='user-avtar']"
    # profile_icon = "//header//a[@class='user-avatar']"
    logout_profile = "//span[normalize-space()='Logout']"
    # logout_profile = "//a[contains(@class,'pc-head-link') and contains(@class,'dropdown-toggle')]"

    def click_all_header_items(self):
        """Click on each header items"""
        for index, item in enumerate(self.header_items, start=1):
            self._click(item)
            self._take_screenshot(f"header_item_{index}")   
 
    def logout_by_button(self):
        """Đăng xuất khỏi hệ thống."""
        self._click(self.btn_logout)
        self._take_screenshot("Logout_by_button")

    def logout_on_profile(self):
        """Đăng xuất khỏi hệ thống."""
        self._click(self.profile_icon)
        self._click(self.logout_profile)
        print("Logout by profile successfully")
        self._take_screenshot("Logout_on_profile")
