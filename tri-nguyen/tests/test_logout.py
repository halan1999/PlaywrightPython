from components.header_components import HeaderComponent
from pages.login_page import LoginPage
from playwright.sync_api import expect, Page, sync_playwright
import time, re
import json

def test_loggout_successfully(perform_login, page):
    # open login page
        login_page = LoginPage(page)
        login_page.goto()
    # login by username / password
        print("đã đăng nhập xong")
    #logout
        logout = HeaderComponent(page)
        logout.test_loggout()
        time.sleep(5)