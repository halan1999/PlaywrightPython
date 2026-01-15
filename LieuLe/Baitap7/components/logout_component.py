from core.base_page import BasePage

class LogoutComponent(BasePage):

    AVATAR = "//img[contains(@class,'user-avtar')]"
    LOGOUT_IN_LIST = "//span[normalize-space()='Logout']"
    LOGOUT_BODY = "//a[contains(text(),'Logout')]"

    def logout_from_header(self):
        self.page.locator(self.AVATAR).click()
        self.page.locator(self.LOGOUT_IN_LIST).click()

    def logout_from_body(self):
        self.page.locator(self.LOGOUT_BODY).click()
