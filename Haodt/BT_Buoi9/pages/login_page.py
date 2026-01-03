from playwright.sync_api import expect

class LoginPage:

    def __init__(self, page):
        self.page = page
        self.social_icons = page.locator("(//*[name()='path'][@class='st0'])[3]")
        self.username = page.locator("//input[@placeholder='Username']")
        self.password = page.locator("//input[@placeholder='Password']")
        self.login_btn = page.locator("//button[normalize-space()='Login']")

    def load(self):
        self.page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    def click_social_icon(self):
        return self.social_icons

    def login(self, user="Admin", pwd="admin123"):
        self.username.fill(user)
        self.password.fill(pwd)
        self.login_btn.click()

