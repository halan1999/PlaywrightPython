from pages.login_page import LoginPage
from pages.home_page import HomePage
from components.header_component import HeaderComponent

def test_login_valid(page):
    login_page = LoginPage(page)
    home_page = HomePage(page)
    header = HeaderComponent(page)

    # Open login page
    login_page.open()

    # Login valid
    login_page.login_valid()
    assert home_page.is_loaded()
    header._user_profile.click()
    header._logout_dropdown_item.click()
    
    # Click each header icons
    header.click_header_icons()

def test_login_valid(page):
    login_page = LoginPage(page)
    home_page = HomePage(page)
    header = HeaderComponent(page)

    # Open login page
    login_page.open()

    # Login invalid
    login_page.login_invalid()
    assert login_page.is_invalid_toast_visible()
    