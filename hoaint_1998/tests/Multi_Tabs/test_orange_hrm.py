from pages.Multi_Tabs.orange_hrm_login import Orange_Hrm_Login
from pages.Multi_Tabs.twitter_organge import TwitterOrange

def test_orage_hrm(page):
    login = Orange_Hrm_Login(page)
    login._go_to_orange_hrm_login()
    linkedin = login._open_linkedin_tab()
    login._bring_to_font()
    facebook = login._open_facebook_tab()
    login._bring_to_font()
    twitter : TwitterOrange = login._open_twitter_tab()
    login._bring_to_font()
    youtube = login._open_youtube_tab()
    login._bring_to_font()
    facebook.bring_to_front()
    youtube.bring_to_front()
    linkedin.bring_to_front()
    twitter._bring_to_font()
    twitter._verify_twitter_orange_page()
    login._bring_to_font()
    login._login()
    login._verify_dashboard_page()
    login._logout()
