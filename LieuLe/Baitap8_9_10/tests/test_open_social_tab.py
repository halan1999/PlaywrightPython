from utils.path_helper import get_avatar_path
import allure

@allure.title("Verify footer social links")
@allure.severity(allure.severity_level.NORMAL)
def test_open_footer_social_tab(login_page):
    with allure.step("Open Login page"):  
        login_page.open()     
    with allure.step("Open all social tabs"):        
        tabs = login_page.open_social_tabs()
    with allure.step("Verify social links"):
        login_page.verify_social_tabs(tabs)

@allure.title("Verify Twitter link and login flow")
@allure.severity(allure.severity_level.CRITICAL)
def test_verify_twitter (login_page):
    # Open login   
    with allure.step("Open login page"): 
        login_page.open()
    # Open twitter tab
    with allure.step("Open twitter tab"):
        twitter_tab = login_page.open_twitter_tab()
    with allure.step("Verify twitter page"):
        login_page.verify_twitter_page(twitter_tab)
    # Back to login tab
    with allure.step("Back to login tab"):
        login_page.footer_component.back_to_login_tab()
    
def test_login_success(login_page):
    # Login
    with allure.step("Login to system"):
        dashboard_page = login_page.open().login_valid_user()
    # Verify dashboard
    with allure.step("Verify dashboard"):
        dashboard_page.verify_dashboard_displayed()
    # Change avatar
    with allure.step("Change avatar"):
        dashboard_page.user_menu.change_avatar("avatar.png")
    # Logout
    with allure.step("Logout!"):
        dashboard_page.user_menu.logout()
