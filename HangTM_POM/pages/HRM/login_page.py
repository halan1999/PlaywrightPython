from playwright.sync_api import Page
from Core.Base_page  import BasePage
#from pages.dashboard_page import DashboardPage
class LoginPage(BasePage):
    URL="https://hrm.anhtester.com/erp/login"
    def __init__(self, page:Page):
        super().__init__(page)
        self.username_input="input[name='iusername']"
        self.password_input="input[name='password']"
        self.login_button="form#erp-form button[type='submit']"
    def open(self) -> None:
        self.goto(self.URL)

    def login(self, username:str, password:str):
        self.fill(self.username_input, username)
        self.fill(self.password_input,password)
        self.click(self.login_button)
    def assert_login_success(self):
        self.should_visible("text=Welcome admin_example hello")
