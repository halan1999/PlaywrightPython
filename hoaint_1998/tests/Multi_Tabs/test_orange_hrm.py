from pages.Multi_Tabs.orange_hrm_login import Orange_Hrm_Login
from pages.Multi_Tabs.twitter_organge import TwitterOrange
import allure

@allure.epic("OrangeHRM")
@allure.description("Verify login and check the tab twitter")
@allure.severity(allure.severity_level.NORMAL)
def test_orage_hrm(page):
    login = Orange_Hrm_Login(page)
    with allure.step("Open login page"):
        login._go_to_orange_hrm_login()
    with allure.step("Open tab twitter"):
        twitter : TwitterOrange = login._open_twitter_tab()
    with allure.step("_verify_twitter_orange_page"):
        twitter._verify_twitter_orange_page()
    with allure.step("_bring_to_font Login"):
        login._bring_to_font()
    with allure.step("Perform Login"):
        login._login()
    with allure.step("_verify_dashboard_page"):
        login._verify_dashboard_page()
    with allure.step("Perform Logout"):
        login._logout()
