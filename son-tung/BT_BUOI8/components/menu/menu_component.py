from BT_BUOI8.core.base_page import BasePage

class MenuComponent(BasePage):

    def open_menu(self, menu):
        self._click(f"//div[@class='navbar-wrapper']//span[normalize-space()='{menu}']", "Menu button")
        self._take_screenshot("Menu_button.png")


