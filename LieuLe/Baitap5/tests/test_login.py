from pages.login_page import LoginPage
from playwright.async_api import expect
import time

def test_login_successfully(page):
    login_page = LoginPage(page)
    login_page.loginwith("standard_user", "secret_sauce")
    time.sleep