import time
from buoi8.pages.login_page import LoginPage
from buoi8.pages.multi_tab.facebook_page import FacebookPage
from buoi8.pages.multi_tab.linkedln_page import LinkedlnPage
from buoi8.pages.multi_tab.twitter_page import TwitterPage
from buoi8.pages.multi_tab.youtube_page import YoutubePage


def test_multiple_tab(login_page :LoginPage):
    main_page = login_page
    main_page.go_to_loginpage()

    assert main_page.get_heading5() == "Login"

    youtube_page: YoutubePage = main_page.open_youtube_tab()
    youtube_page.assert_visible_youtube_channel()
    # facebook_page = main_page.open_facebook_tab()
    # facebook_page.assert_visible_facebook_name()
    main_page._bring_to_front()
    assert main_page.get_heading5() == "Login"

    facebook_page: FacebookPage = main_page.open_facebook_tab()
    facebook_page.assert_visible_facebook_url()
    main_page._bring_to_front()
    assert main_page.get_heading5() == "Login"

    twitter_page: TwitterPage = main_page.open_twitter_tab()
    twitter_page.assert_visible_twitter()
    main_page._bring_to_front()
    assert main_page.get_heading5() == "Login"

    facebook_page: LinkedlnPage = main_page.open_linkedin_tab()
    facebook_page.assert_visible_linkedln_name()
    main_page._bring_to_front()
    assert main_page.get_heading5() == "Login"