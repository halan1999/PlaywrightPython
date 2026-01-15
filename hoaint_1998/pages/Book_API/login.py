from core.base_page import BasePage

class Login(BasePage):
    def __init__(self, page):
        super().__init__(page)

    def login(self, email: str, password: str):
        EMAIL = self.page.get_by_role("textbox", name="Email address")
        PASSWORD = self.page.get_by_role("textbox", name="Password")
        LOGIN_BUTTON = self.page.get_by_role("button", name="Login account")
        # perform login
        EMAIL.fill(email)
        PASSWORD.fill(password)
        LOGIN_BUTTON.click()

        