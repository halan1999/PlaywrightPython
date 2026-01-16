from playwright.sync_api import expect

class LoginPage:
    EMAIL = "input[name='email']"
    PASSWORD = "input[name='password']"
    LOGIN_BTN = "button[type='submit']"
    SUCCESS_TOAST = ".toast-success"

    def __init__(self, page):
        self.page = page

    def login(self, email, password):
        self.page.fill(self.EMAIL, email)
        self.page.fill(self.PASSWORD, password)
        self.page.wait_for_timeout(500)
        self.page.click(self.LOGIN_BTN)
        self.page.wait_for_timeout(500)

    def is_login_success(self):
        toast = self.page.get_by_text("Login successfully", exact=False)
        toast.wait_for(timeout=5000)
        return True
