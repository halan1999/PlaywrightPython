from pages.hrm_anhtester.home_page import HomePage
from pages.hrm_anhtester.login_page import LoginPage
from playwright.sync_api import expect
import re

def test_logout_via_button(logged_in_page):
    home_page = HomePage(logged_in_page)
    home_page.logout()   

    login = LoginPage(logged_in_page)
    login.is_loaded()                   
    expect(logged_in_page).to_have_url(re.compile(r"/login"))
