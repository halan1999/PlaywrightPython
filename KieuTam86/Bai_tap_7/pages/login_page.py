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

    def login_valid_user(self):
        creds = self.load_credentials()
        valid_user = creds["valid_user"]
        self.goto()
        self._fill(self.username_locator, valid_user["username"])
        self._fill(self.password_locator, valid_user["password"])
        self._take_screenshot("Input_User_Password")
        self._click(self.btn_Login_locator)
        time.sleep(5)
        self._take_screenshot("Home")

    def run_header_flow(self):
        self.header.click_all_header_items()

    def logout(self):
        self.header.logout_by_button()
        self._take_screenshot("After_logout")
        print(f"Logout successfully!")   

    def login_fail(self):
        creds = self.load_credentials()
        invalid_user = creds["invalid_user"]
        self.goto()
        self._fill(self.username_locator, invalid_user["username"])
        self._fill(self.password_locator, invalid_user["password"])
        self._take_screenshot("Fill_invalide_user")
        self._click(self.btn_Login_locator)
        time.sleep(3)
        # self._verify_visible(self.Ladda_Progress)
        self._take_screenshot("Login_Fail")







