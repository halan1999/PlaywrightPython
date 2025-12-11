from playwright.sync_api import Page,expect
from pages.login_page import LoginPage
from config.social_network_links_enum import SocialNetworkLinks
from pages.twitter_orange_page import TwitterOrangePage

BASE_URL = "https://opensource-demo.orangehrmlive.com/web/index.php/"
LOGIN_URL = f"{BASE_URL}auth/login"

def test_3_back_from_twitter_then_login_successfully_and_logout(page: Page):
    login_page = LoginPage(page)
    login_page.go_to_page(LOGIN_URL)

    new_tab_page = login_page.open_social_link(SocialNetworkLinks.TWITTER)

    TwitterOrangePage(new_tab_page)
    # UNABLE TO USE BRING TO FRONT???????? -- @HA LAN
    new_tab_page.close()

    dashboard_url = f"{BASE_URL}dashboard/index"
    username = "Admin"
    password = "admin123"

    home_page = login_page.login(username,password)
    expect(page).to_have_url(dashboard_url)

    home_page.logout()
    login_url = f"{BASE_URL}auth/login"
    expect(page).to_have_url(login_url)
