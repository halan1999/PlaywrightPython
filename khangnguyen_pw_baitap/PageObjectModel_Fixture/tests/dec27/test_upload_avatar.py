import os
import allure

from pages.hrm_anhtester.login_page import LoginPage
from pages.hrm_anhtester.home_page import HomePage
from pages.hrm_anhtester.account_settings_page import AccountSettingsPage
from components.hrm_anhtester.header_component import HeaderComponent

@allure.title("Upload profile picture with valid file")
@allure.description(
    "Verify user can upload profile picture with a valid file type and file name appears in header avatar image."
)
def test_upload_profile_picture_with_valid_file_type(page):
    login_page = LoginPage(page)
    home_page = HomePage(page)
    account_settings = AccountSettingsPage(page)
    header = HeaderComponent(page)

    image_path = "resources/images/test111.jpg"
    expected_file_name = os.path.basename(image_path)

    with allure.step("Login with valid account"):
        login_page.open()
        login_page.is_login_page_loaded()
        login_page.login_valid()

    with allure.step("Go to Account Settings page"):
        home_page.click_profile_link()

    with allure.step("Open Profile Picture tab"):
        account_settings.click_tab("Profile Picture")

    with allure.step("Upload a valid file"):
        account_settings.upload_profile_picture(image_path)
        account_settings.wait_the_upload_is_completed(image_path)

    with allure.step("Click Update Picture button"):
        account_settings.click_update_picture()

    with allure.step("Verify uploaded file name appears in header avatar"):
        header.verify_avatar_src_contains(expected_file_name, timeout=10000)