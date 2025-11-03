from playwright.sync_api import Page
from pages.login_page import LoginPage

def test_add_product(page : Page):
    USERNAME = 'standard_user'
    PASSWORD = 'secret_sauce'

    page.goto('https://www.saucedemo.com/')

    try:
        login_page = LoginPage(page)
        login_page.login(USERNAME, PASSWORD)
        login_page.assert_login_pass()
    except:
        raise ValueError('Đăng nhập không thành công với tài khoản: {USERNAME}')
    
    