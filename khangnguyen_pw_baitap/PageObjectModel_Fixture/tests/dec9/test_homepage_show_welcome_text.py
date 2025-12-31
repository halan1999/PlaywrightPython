from pages.hrm_anhtester.login_page import LoginPage
from pages.hrm_anhtester.home_page import HomePage

def test_homepage_show_welcome_text(logged_in_page):
    home_page = HomePage(logged_in_page)
    assert home_page.is_homepage_loaded()
