from playwright.sync_api import Page
from pages.twitter_page import TwitterPage
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage

def test_click_icons_and_verify_button_and_title_for_twitter(HRMLoginPage):

    facebook_page = HRMLoginPage.open_social_tab(LoginPage.FACEBOOK_ICON)
    facebook_page.screenshot(path = 'screenshots/facebook.png')
    HRMLoginPage._back_to_login_page()
    
    twitter_page = HRMLoginPage.open_social_tab(LoginPage.TWITTER_ICON)
    twitter_page.screenshot(path = 'screenshots/twitter.png')
    twitter_page = TwitterPage(twitter_page)
    twitter_page.assert_title_visible()
    twitter_page.assert_top_left_x_visible()
    HRMLoginPage._back_to_login_page()

    linkedin_page = HRMLoginPage.open_social_tab(LoginPage.LINKEDIN_ICON)
    linkedin_page.screenshot(path = 'screenshots/linkedin.png')
    HRMLoginPage._back_to_login_page()

    youtube_page = HRMLoginPage.open_social_tab(LoginPage.YOUTUBE_ICON)
    youtube_page.screenshot(path = 'screenshots/youtube.png')
    HRMLoginPage._back_to_login_page()

def test_e2e_flow(page):
    login_page = LoginPage(page)
    login_page.goto()
    login_page.login("Admin", "admin123")

    dashboard_page = DashboardPage(page)
    dashboard_page.assert_dashboard_visible()
    dashboard_page.logout()
