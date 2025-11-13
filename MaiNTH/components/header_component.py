from core.base_page import BasePage
class Header_component(BasePage):
    def __init__(self, page):
        super().__init__(page)  # ✅ thừa hưởng page + click()

    header_item = [
        "//header//a[@data-original-title= 'Account Settings']",
        "//header//span[@data-original-title= 'Apps']",
        "//header//a[@data-original-title= 'System Calendar']",
        "//header//a[@data-original-title= 'System Reports']",
        "//li//a[@data-toggle='dropdown']//img[contains(@src,'languages')]",
        "//li//a[@data-original-title='Todo List']"  
    ]
    logout_button = "//span[contains(text(),'Logout')]"
    profile_icon = "//li//a[@data-toggle='dropdown']//img[contains(@src,'users')]"
    my_account = "//span[contains(text(),'My Account')]"
    
    def click_all_header_items(self):
        for index, item in enumerate(self.header_item, start=1):
            print(f"[INFO] Click header item {index}: {item}")
            self._click(item, f"header_item_{index}")  # ✅ dùng đúng biến
            self._take_screenshot(f"header_item_{index}")


    def log_out(self):
        self._click(self.profile_icon)
        self._click(self.logout_button)