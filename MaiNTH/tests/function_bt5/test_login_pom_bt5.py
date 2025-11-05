from playwright.sync_api import expect
from pages.login_page import LoginPage
def test_login_successfully(page) -> None:
    login_page = LoginPage(page)
    # Step 1: Visit login page
    login_page.visit_login_page()
    # Step 2: Perform login action
    login_page.login("standard_user", "secret_sauce")
    # Step 3: Verify successful login by checking URL
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
    print("Login test passed successfully")

def test_login_invalid_user(page) -> None:
    login_page = LoginPage(page)
    # Step 1: Visit login page
    login_page.visit_login_page()
    # Step 2: Perform login action with invalid credentials
    login_page.login("invalid_user", "wrong_password")
    # Step 3: Verify error message is displayed
    login_page._assert_text_visible(
        LoginPage.ERROR_MESSAGE,
        "Epic sadface: Username and password do not match any user in this service"
    )   
    print("Invalid login test passed successfully")
def test_login_empty_password(page) -> None:
    login_page = LoginPage(page)
    # Step 1: Visit login page
    login_page.visit_login_page()
    # Step 2: Perform login action with empty password
    login_page.login("standard_user", "")
    # Step 3: Verify error message is displayed
    login_page._assert_text_visible(
        LoginPage.ERROR_MESSAGE,
        "Epic sadface: Password is required"
    )   
    print("Empty password login test passed successfully")
def test_login_empty_username(page) -> None:
    login_page = LoginPage(page)
    # Step 1: Visit login page
    login_page.visit_login_page()
    # Step 2: Perform login action with empty username
    login_page.login("", "secret_sauce")
    # Step 3: Verify error message is displayed
    login_page._assert_text_visible(
        LoginPage.ERROR_MESSAGE,
        "Epic sadface: Username is required"
    )   
    print("Empty username login test passed successfully")
def test_login_empty_username_password(page) -> None:
    login_page = LoginPage(page)
    # Step 1: Visit login page
    login_page.visit_login_page()
    # Step 2: Perform login action with empty username and password
    login_page.login("", "")
    # Step 3: Verify error message is displayed
    login_page._assert_text_visible(
        LoginPage.ERROR_MESSAGE,
        "Epic sadface: Username is required"
    )   
    print("Empty username and password login test passed successfully")
    