from pages.orange_hrm_page import Oranage_HRM
from pages.dash_board import Dashboard
from components.social_footer import Social_Footer
from playwright.sync_api import Playwright

def test_multi_tab_twister_and_login(page):

    orangeORM_page = Oranage_HRM(page)
    social = Social_Footer(page)

    # 1. Open page
    orangeORM_page.goto()

    # 2. Click Twitter icon -> new tab
    twister_tab = orangeORM_page.click_icon_twister()

    # 3. Verify Twitter tab
    social.verify_twister_page(twister_tab)

    # 4. Close Twitter & back to main tab
    twister_tab.close()
    orangeORM_page.bring_to_front()

    # 5. Login
    orangeORM_page.login_valid_user()

    # 6. Verify Dashboard
    orangeORM_page.verify_dashboard()

    # 7. Logout
    orangeORM_page.logout()

def test_multi_tab_facebook_and_login(page):

    orangeORM_page = Oranage_HRM(page)
    social = Social_Footer(page)

    # 1. Open page
    orangeORM_page.goto()

    # 2. Click Twitter icon -> new tab
    facebook_tab = orangeORM_page.click_icon_facebook()

    # 3. Verify Twitter tab
    social.verify_facebook_page(facebook_tab)

    # 4. Close Twitter & back to main tab
    facebook_tab.close()
    orangeORM_page.bring_to_front()

    # 5. Login
    orangeORM_page.login_valid_user()

    # 6. Verify Dashboard
    orangeORM_page.verify_dashboard()

    # 7. Logout
    orangeORM_page.logout()

def test_multi_tab_youtube_and_login(page):

    orangeORM_page = Oranage_HRM(page)
    social = Social_Footer(page)

    # 1. Open page
    orangeORM_page.goto()

    # 2. Click Twitter icon -> new tab
    youtube_tab = orangeORM_page.click_icon_youtube()

    # 3. Verify Twitter tab
    social.verify_youtube_page(youtube_tab)

    # 4. Close Twitter & back to main tab
    youtube_tab.close()
    orangeORM_page.bring_to_front()

    # 5. Login
    orangeORM_page.login_valid_user()

    # 6. Verify Dashboard
    orangeORM_page.verify_dashboard()

    # 7. Logout
    orangeORM_page.logout()

