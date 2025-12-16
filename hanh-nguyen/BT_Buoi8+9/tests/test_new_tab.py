from core.base_page import BasePage
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage

def test_click_icons(HRMLoginPage):

    facebook_page = HRMLoginPage.open_social_tab(LoginPage.FACEBOOK_ICON)
    facebook_page.screenshot(path = 'screenshots/facebook.png')

    twitter_page = HRMLoginPage.open_social_tab(LoginPage.TWITTER_ICON)
    twitter_page.screenshot(path = 'screenshots/twitter.png')

    linkedin_page = HRMLoginPage.open_social_tab(LoginPage.LINKEDIN_ICON)
    linkedin_page.screenshot(path = 'screenshots/linkedin.png')

    youtube_page = HRMLoginPage.open_social_tab(LoginPage.YOUTUBE_ICON)
    youtube_page.screenshot(path = 'screenshots/youtube.png')


def test_verify_displaying_title_and_x_icon(page):
    twitter_page = TwitterPage(page)
    twitter_page.assert_title_visible()
    twitter_page.assert_top_left_x_visible()

def test_e2e_flow(page):
    login_page = LoginPage(page)
    login_page.goto()
    login_page.login("Admin", "admin123")

    dashboard_page = DashboardPage(page)
    dashboard_page.assert_dashboard_visible()
    dashboard_page.logout()
