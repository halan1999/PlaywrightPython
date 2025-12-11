from playwright.sync_api import Page,expect
from pages.login_page import LoginPage
from pages.social_network_page import SocialNetworkPage
from config.social_network_links_enum import SocialNetworkLinks
from pages.twitter_orange_page import TwitterOrangePage

BASE_URL = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"

def test_navigation_social_links(page:Page):
    login_page = LoginPage(page)

    login_page.go_to_page(BASE_URL)

    for item in SocialNetworkLinks:
        xpath = item.value[0]
        expect_url = item.value[1]

        new_tab_page = login_page.open_social_link(item)
        social_page = SocialNetworkPage(new_tab_page)
        current_url = social_page._get_page_url()

        print(f"URL hiện tại: {current_url}, URL mong đợi: {expect_url}")
        assert expect_url in current_url, f"Lỗi: URL không khớp. Hiện tại: {current_url}, Mong đợi chứa: {expect_url}"
        # Đóng tab mới để chuẩn bị cho lần lặp tiếp theo
        new_tab_page.close()

def test_open_twitter_and_verify_page(page: Page, base_url):
    login_page = LoginPage(page)
    login_page.go_to_page(BASE_URL)
    
    new_tab_page = login_page.open_social_link(SocialNetworkLinks.TWITTER)
    
    twitter_page = TwitterOrangePage(new_tab_page)
    twitter_page.verify_twitter_orange_page()