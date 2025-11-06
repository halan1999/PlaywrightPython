from pages.login_page import LoginPage
from pages.home_page import HomePage
from components.header_components import HeaderComponent
from resources.credentials_loader import get_valid

def test_login_with_valid_credentials(page):
    # Get invalid credentials from JSON file
    username, password = get_valid()

    login_page = LoginPage(page)
    home_page = HomePage(page)
    header_component = HeaderComponent(page)

    # Open login page
    login_page.open()
    login_page.take_screenshot("login_page.png")

    # Login
    login_page.login(username, password)
    login_page.take_screenshot("input_credentials.png")


    # Expected: Home page is loaded
    assert home_page.is_loaded()
    # Take a screenshot of home page
    home_page.take_screenshot("home_page.png")

    # Click Account Settings in header
    header_component._click_account_settings_icon()
    home_page.take_screenshot("account_settings.png")

    # Click Apps in header
    header_component._click__apps_icon()
    home_page.take_screenshot("apps_dropdown_list.png")

    # Click System Calendar in header
    header_component._click__system_calendar_icon()
    home_page.take_screenshot("system_calendar.png")

    # Click System Report in header
    header_component._click__system_reports()
    home_page.take_screenshot("system_report.png")


