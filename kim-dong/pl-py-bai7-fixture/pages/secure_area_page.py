from pages.base_page import BasePage

class SecureAreaPage(BasePage):
    LOGOUT_LINK = "a[href='/logout']"
    FLASH_MESSAGE = "#flash"

    def logout(self):
        print("[Click] Logout link")
        self._click(self.LOGOUT_LINK)
        from pages.login_page import LoginPage
        return LoginPage(self.page)

    @property
    def flash_message(self):
        return self.page.locator(self.FLASH_MESSAGE)
