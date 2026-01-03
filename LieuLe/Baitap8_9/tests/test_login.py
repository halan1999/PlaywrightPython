
from playwright.sync_api import Playwright
from LieuLe.Baitap8_9.pages.login.login_page import LoginPage

def test_login(login_page):
    login_page.login_valid_user()
    