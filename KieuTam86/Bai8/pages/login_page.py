from core.base_page import BasePage, expect
from components.header_component import HeaderComponent
from pages.forgot_password_page import ForgotPassword
from components.your_apps_component import YourApps
import time, json

class LoginPage(BasePage):
    #Save locator & action of Login page

    url = "https://hrm.anhtester.com/erp/login"
    username_locator = "#iusername"
    username_placeholder = "//input[@placeholder='Your Username']"
    password_locator = "#ipassword"
    btn_Login_locator = "//button[@type='submit']"
    # Btn_Logout = "//a[@class='btn btn-smb btn-outline-primary rounded-pill']"
    title_locator = "//h4[normalize-space() = 'Welcome to HRM | Anh Tester Demo']"
    title_message = 'Welcome to HRM | Anh Tester Demo'
    textmuted_locator= "//p[normalize-space() = 'Welcome back, Please login into an account']"
    textmuted_message = 'Welcome back, Please login into an account'
    username_visible = "Your Username"
    password_visible = "Enter Password"
    forgot_locator = "//span[normalize-space() = 'Forgot password?']"
    forgot_visible = "Forgot password?"
    toast_message_locator = ".toast-message"
    error_message_password_short = "Your password is too short, minimum 6 characters required."
    error_messag_invalid_user = "Invalid Login Credentials."


    def __init__(self, page):
        super().__init__(page)
        # self.header = HeaderComponent(page)

    def load_credentials(self):
        with open("data/credentials.json","r") as f:
            return json.load(f)

    def goto(self):
        self._open_page(self.url)
        self._take_screenshot("Open_login_page")

    def  check_form_login(self):
        self.goto()
        self._verify_locator_visible(self.title_locator)
        self._verify_locator_visible(self.username_locator)
        self._verify_locator_visible(self.password_locator)
        self._verify_locator_visible(self.forgot_locator)
        self._verify_locator_visible(self.btn_Login_locator)

        self._verify_text(self.title_locator, self.title_message)
        self._verify_placeholder(self.username_locator, self.username_visible)
        self._verify_placeholder(self.password_locator, self.password_visible)
        self._verify_text(self.forgot_locator, self.forgot_visible)
        self._verify_text(self.btn_Login_locator,"Login")

    def login_valid_user(self):
        creds = self.load_credentials()
        self.goto()
        self._fill(self.username_locator, creds["valid_user"]["username"])
        self._fill(self.password_locator, creds["valid_user"]["password"])
        self._take_screenshot("Input_User_Password")
        self._click(self.btn_Login_locator)
        time.sleep(3)
        self._take_screenshot("Home")

    def login_fail_username(self):
        creds = self.load_credentials()
        self.goto()
        self._fill(self.username_locator, creds["invalid_user"]["username"])
        self._fill(self.password_locator, creds["invalid_user"]["password"])
        self._click(self.btn_Login_locator)
        
        time.sleep(3) 
        self._take_screenshot("Login_Fail_Username")
        self._verify_locator_visible(self.toast_message_locator)
        self._verify_text(self.toast_message_locator, self.error_messag_invalid_user)
        print(f"[ERROR_MESSAGE] displays '{self.error_messag_invalid_user}' ")
       
        
    def login_fail_password(self):
        creds = self.load_credentials()
        self.goto()
        self._fill(self.username_locator, creds["invalid_password"]["username"])
        self._fill(self.password_locator, creds["invalid_password"]["password"])
        self._click(self.btn_Login_locator)
        time.sleep(3)
        self._take_screenshot("Login_Fail_Password")
        self._verify_locator_visible(self.toast_message_locator)
        self._verify_text(self.toast_message_locator, self.error_messag_invalid_user)
        print(f"[ERROR_MESSAGE] displays '{self.error_messag_invalid_user}' ")

    def login_password_short(self):
        creds = self.load_credentials()
        self.goto()
        self._fill(self.username_locator, creds["short_password"]["username"])
        self._fill(self.password_locator, creds["short_password"]["password"])
        self._click(self.btn_Login_locator)
        time.sleep(3)
        self._take_screenshot("Login_Fail_Password")
        self._verify_locator_visible(self.toast_message_locator)
        self._verify_text(self.toast_message_locator, self.error_message_password_short)
        print(f"[ERROR_MESSAGE] displays '{self.error_message_password_short}' ")

    def goto_forgot_password(self):
        self.goto()
        self._click(self.forgot_locator)
        forgot_pass = ForgotPassword(self.page)
        self._take_screenshot("Go_to_Forgot_Password")
        forgot_pass.check_form_forgot_password()

    def goto_Your_apps_items_menu(self):
        your_apps = YourApps(self)
         

    # def click_all_header(self):
    #     self.header.click_all_header_items()






