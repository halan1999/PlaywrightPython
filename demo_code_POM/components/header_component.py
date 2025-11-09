# components/header_component.py
from core.base_page import BasePage

class HeaderComponent(BasePage):

    header_items = [
        "//header//a[@data-original-title='Account Settings']",
        "//header//span[@data-original-title='Apps']",
        "//header//a[@data-original-title='System Calendar']",
        "//header//a[@data-original-title='System Reports']",
        "//header//li[1]//a[@data-toggle='dropdown']",
        "//header//li[1]//a[@data-toggle='tooltip']"
    ]


    logout_button = "//span[normalize-space()='Logout']"
    profile_icon = "//header//a/*[@class='user-avtar']"
    icon = "//a[@class='b-brand']//img[@class='logo logo-lg']"

    def wait_for_user_logged_in(self):
        self._wait_for_visible(self.icon)

    def click_all_header_items(self):
        for index, item in enumerate(self.header_items, start=1):
            self._click(item)
            self._take_screenshot(f"header_item_{index}")

    def logout(self):
        self._click(self.profile_icon)
        self._click(self.logout_button)
