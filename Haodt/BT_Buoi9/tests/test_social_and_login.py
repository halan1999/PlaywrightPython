import pytest
from playwright.sync_api import Page, BrowserContext, expect
from pages.login_page import LoginPage
from pages.social_page import SocialPage
from pages.dashboard_page import DashboardPage


def test_social_icon_twitter_and_login(
        login: LoginPage,
        context: BrowserContext,
        social_page,
        dashboard_page
    ):
    
    main_page = login.page 

    with context.expect_page() as new_tab_info:
        login.click_social_icon().click() 
    twitter_tab = new_tab_info.value
    twitter_tab.bring_to_front()

    sp = social_page(twitter_tab)
    sp.verify_twitter_page()

    twitter_tab.close()

    main_page.bring_to_front()

    login.login()

    dashboard = dashboard_page(main_page)
    dashboard.verify_dashboard()

    dashboard.logout()
