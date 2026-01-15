from pages.dashboard.dashboard_page import DashboardPage 
import allure 

@allure.title("Verify login with valid credentials")
@allure.severity(allure.severity_level.CRITICAL)
def test_login(login_page):
    dashboard_page = DashboardPage(login_page.page)
    with allure.step("Open login page"):
        login_page.open()

    with allure.step("Login with valid user"):
        login_page.login_valid_user()
    
    with allure.step("Verify dashboard displayed"):
        dashboard_page.verify_dashboard_displayed()
    
