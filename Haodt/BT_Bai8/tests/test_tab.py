from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage
from pages.multiple_page import SocialPage
import time

def test_social_links(page, context):

    login = LoginPage(page)
    login.load()

    main_page = page  # tab chính
    icons = login.get_all_social_icons()  # các icon social

    # Expected text mapping theo từng icon
    expected_texts = [
        "OrangeHRM",                                          # X.com
        "OrangeHRM Inc"                                      # YouTube
    ]

    # duyệt từng icon
    for i in range(icons.count()):

        # --- CLICK ICON ĐỂ MỞ TAB MỚI ---
        with context.expect_page() as new_tab_info:
            icons.nth(i).click()

        new_page = new_tab_info.value
        new_page.bring_to_front()

        # --- VERIFY TRONG TAB MỚI ---
        social = SocialPage(new_page)
        social.verify_heading(expected_texts[i])

        # --- ĐÓNG TAB MỚI ---
        new_page.close()

        # --- QUAY VỀ TAB CHÍNH ---
        main_page.bring_to_front()

        # OPTIONAL: đợi 1 chút để UI ổn định
        page.wait_for_timeout(500)
    
