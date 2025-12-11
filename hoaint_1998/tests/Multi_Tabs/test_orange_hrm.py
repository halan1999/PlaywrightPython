from pages.Multi_Tabs.orange_hrm_login import Orange_Hrm_Login
from pages.Multi_Tabs.twitter_organge import TwitterOrange

def test_orage_hrm(page):
    login = Orange_Hrm_Login(page)
    login._go_to_orange_hrm_login()
    twitter : TwitterOrange = login._open_twitter_tab()
    twitter._verify_twitter_orange_page()
    login._bring_to_font()
    login._login()
    login._verify_dashboard_page()
    login._logout()
