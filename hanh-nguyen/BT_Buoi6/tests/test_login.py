from pages.login_page import LoginPage
from playwright.sync_api import Playwright

def test_login_successfully():
    loginPage = LoginPage()
    loginPage.open()
    cred = loginPage.read_credentials()
    loginPage.login(cred["valid_user"]["username"], cred["valid_user"]["password"])

def account_setting():
    loginPage = LoginPage()
    loginPage.open()
    cred = loginPage.read_credentials()
    loginPage.login(cred["valid_user"]["username"], cred["valid_user"]["password"])
