import time
from buoi9.pages.dashboard_page import DashBoardPage
from buoi9.pages.login_page import LoginPage

from buoi9.pages.multi_tab.twitter_page import TwitterPage



def test_multiple_tab(login_page :LoginPage):
    main_page = login_page
    main_page.go_to_loginpage()

    assert main_page.get_heading5() == "Login"

    twitter_page: TwitterPage = main_page.open_twitter_tab()
    twitter_page.assert_visible_twitter()
    main_page._bring_to_front()
    assert main_page.get_heading5() == "Login"
    # main_page.logged()
    dashboard_page: DashBoardPage = main_page.logged()
    dashboard_page.assert_dashboard_screen()
    dashboard_page.assert_loggout_successfully()

   