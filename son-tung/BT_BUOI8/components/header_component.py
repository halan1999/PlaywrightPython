from BT_BUOI8.core.base_page import BasePage

class HeaderComponent(BasePage):
    APP_HEADER_BUTTON = "//header//span[@data-original-title='Apps']"
    LANGUAGE_BUTTON = "//header//a[@data-toggle='dropdown'][1]//img[contains(@src, 'languages_flag')]"
    LOGOUT_BUTTON = "//header//img[@class='user-avtar']"

    def open_all_button(self):
        lst_button = ["Account Settings", "System Calendar", "System Reports", "Todo List"]
        for btn in lst_button:
            self._click(f"//header//a[@data-original-title='{btn}']", "Header button")
            self._take_screenshot("Header button.png")

    def open_app_list_button(self):
        self._click(self.APP_HEADER_BUTTON, "Apps button")
        self._take_screenshot("App button.png")

    def open_language_list_button(self):
        self._click(self.LANGUAGE_BUTTON, "Languages button")
        self._take_screenshot("language button.png")

    def logout(self):
        self._click(self.LOGOUT_BUTTON, "Logout button")
        self._take_screenshot("Header button.png")


