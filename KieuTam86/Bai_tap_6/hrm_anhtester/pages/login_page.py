from core.base_page import BasePage, expect
from components.header_component import HeaderComponent
import time, json

class LoginPage(BasePage):
    #Save locator & action of Login page

    url = "https://hrm.anhtester.com/erp/login"
    username_locator = "#iusername"
    password_locator = "#ipassword"
    btn_Login_locator = "//button[@type='submit']"
    link_forgot_pass = "//a[@class='text-primary']"
    ladda_Progress = "//div[@class='ladda-progress']"
    error_message = "Invalid Login credential"
    # Btn_Logout = "//a[@class='btn btn-smb btn-outline-primary rounded-pill']"
    toast_message = ".toast-message"

    def __init__(self, page):
        super().__init__(page)
        self.header = HeaderComponent(page)

    def load_credentials(self):
        with open("data/credentials.json","r") as f:
            return json.load(f)

    def goto(self):
        self._open_page(self.url)
        self._take_screenshot("Open_login_page")

    def login_success(self):
        creds = self.load_credentials()
        self.goto()
        self._fill(self.username_locator, creds["username"])
        self._fill(self.password_locator, creds["password"])
        self._take_screenshot("Input_User_Password")
        self._click(self.btn_Login_locator)
        time.sleep(5)
        self._take_screenshot("Home")

    # def login_fail(self, username, password):
    #     creds = self.load_credentials()
    #     self.goto()
    #     self._fill(self.username_locator, username)
    #     self._fill(self.password_locator, password)
    #     self._click(self.btn_Login_locator)
    #     time.sleep(5)
    #     # self._verify_visible(self.Ladda_Progress)
    #     self._take_screenshot("Login_Fail")







