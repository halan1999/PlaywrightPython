from playwright.sync_api import expect
from config.urls import LOGIN_URL
from LieuLe.Baitap8_9.utils.json_reader import read_json


class LoginComponent:
    EMAIL_INPUT = "input[name='username']"
    PASSWORD_INPUT = "input[name='password']"
    LOGIN_BUTTON = "button[type='submit']"

    def __init__(self, page):
        self.page = page

    def login_valid_user(self):
        data = read_json("data/login_acc.json")
        user = data["valid_user"]

        # ALWAYS go to login page
        self.page.goto(LOGIN_URL)

        # Wait input appear
        expect(self.page.locator(self.EMAIL_INPUT)).to_be_visible()

        self.page.fill(self.EMAIL_INPUT, user["username"])
        self.page.fill(self.PASSWORD_INPUT, user["password"])
        self.page.click(self.LOGIN_BUTTON)
