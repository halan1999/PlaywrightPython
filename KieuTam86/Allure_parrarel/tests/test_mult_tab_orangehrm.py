from pages.orange_hrm_page import Oranage_HRM
from pages.dash_board import Dashboard
from components.social_footer import Social_Footer
from playwright.sync_api import Playwright
import pytest
import allure


@allure.title("Login and open multiple tab -> Open tab Twister")
@allure.description("Verify open tab Twister and verify user can login and see dashboard.")
@allure.severity(allure.severity_level.CRITICAL)
def test_multi_tab_twister_and_login(page):

    orangeORM_page = Oranage_HRM(page)
    social = Social_Footer(page)

    # 1. Open page
    with allure.step("Go to orangeORM page"):
        orangeORM_page.goto()

    # 2. Click Twitter icon -> new tab
    with allure.step("Click on icon Twister on footer"):
        twister_tab = orangeORM_page.click_icon_twister()

    # 3. Verify Twitter tab
    with allure.step("Verify new tab : Twister"):
        social.verify_twister_page(twister_tab)

    # 4. Close Twitter & back to main tab
    with allure.step("Close tab Twister"):
        twister_tab.close()
    with allure.step("Bring Orange Page to front"):
        orangeORM_page.bring_to_front()

    # 5. Login
    with allure.step("Login on Orange page with valid user"):
        orangeORM_page.login_valid_user()

    # 6. Verify Dashboard
    with allure.step("Verify go to Dashboard page"):
        orangeORM_page.verify_dashboard()

    # 7. Logout
    with allure.step("Logout"):
        orangeORM_page.logout()

@allure.title("Login and open multiple tab -> Open tab Facebook")
@allure.description("Verify open tab Facebook and verify user can login and see dashboard.")
@allure.severity(allure.severity_level.CRITICAL)
def test_multi_tab_facebook_and_login(page):


    orangeORM_page = Oranage_HRM(page)
    social = Social_Footer(page)

    # 1. Open page
    with allure.step("Go to orangeORM page"):
        orangeORM_page.goto()

    # 2. Click Twitter icon -> new tab
    with allure.step("Click icon facebook on Orange ORM page"):
        facebook_tab = orangeORM_page.click_icon_facebook()

    # 3. Verify Twitter tab
    with allure.step("Verify Facebook page"):
        social.verify_facebook_page(facebook_tab)

    # 4. Close Twitter & back to main tab
    with allure.step("Close tab Facebook"):
        facebook_tab.close()
    with allure.step("Bring Orange ORM page to front"):
        orangeORM_page.bring_to_front()

    # 5. Login
    with allure.step("Login on Orange ORM page is successfully!"):
        orangeORM_page.login_valid_user()

    # 6. Verify Dashboard
    with allure.step("Verify Dashboard page after login successfully!"):
        orangeORM_page.verify_dashboard()

    # 7. Logout
    with allure.step("Verify logout successfully"):
        orangeORM_page.logout()

@allure.title("Login and open multiple tab -> Open tab Youtube")
@allure.description("Verify open tab Youtube and verify user can login and see dashboard.")
@allure.severity(allure.severity_level.CRITICAL)
def test_multi_tab_youtube_and_login(page):
    
    orangeORM_page = Oranage_HRM(page)
    social = Social_Footer(page)

    # 1. Open page
    with allure.step("Go to orangeORM page"):
        orangeORM_page.goto()

    # 2. Click Twitter icon -> new tab
    with allure.step("Click icon Youtube on Orange ORM page"):
        youtube_tab = orangeORM_page.click_icon_youtube()

    # 3. Verify Twitter tab
    with allure.step("Verify Twister page"):
        social.verify_youtube_page(youtube_tab)

    # 4. Close Twitter & back to main tab
    with allure.step("Close tab Youtube"):
        youtube_tab.close()
    with allure.step("Bring Orange ORM page to front"):
        orangeORM_page.bring_to_front()

    # 5. Login
    with allure.step("Login on Orange ORM page is successfully!"):
        orangeORM_page.login_valid_user()

    # 6. Verify Dashboard
    with allure.step("Verify Dashboard page after login successfully!"):
        orangeORM_page.verify_dashboard()

    # 7. Logout
    with allure.step("Verify logout successfully"):
        orangeORM_page.logout()

