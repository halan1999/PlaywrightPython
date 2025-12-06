from pages.Multi_Tabs.orange_hrm_login import Orange_Hrm_Login

def test_orage_hrm(page):
    login = Orange_Hrm_Login(page)
    login._go_to_orange_hrm_login()
    linkedin = login._open_linkedin_tab()
    login._bring_to_font()
    facebook = login._open_facebook_tab()
    login._bring_to_font()
    twitter = login._open_twitter_tab()
    login._bring_to_font()
    youtube = login._open_youtube_tab()
    login._bring_to_font()
    facebook.bring_to_front()
    youtube.bring_to_front()
    linkedin.bring_to_front()
    twitter.bring_to_front()