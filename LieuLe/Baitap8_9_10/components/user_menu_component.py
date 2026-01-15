from playwright.sync_api import expect
from config.urls import LOGIN_URL
import re
import os

class UserMenuComponent:
    USER_DROPDOWN = "//span[contains(@class,'oxd-userdropdown-tab')]"
    PROFILE_ITEM = "//a[normalize-space()='My Info']"
    LOGOUT_ITEM = "//a[normalize-space()='Logout']"
    AVATAR_INPUT = "//input[@type='file']"
    SAVE_BUTTON = "//button[normalize-space()='Save']"
    AVATAR_ICON = "//img[contains(@class,'employee-image')]"
    CHANGE_ICON = "//i[contains(@class,'bi-plus')]"

    def __init__(self, page):
        self.page = page

    def open_menu(self):
        dropdown = self.page.locator(self.USER_DROPDOWN)
        expect(dropdown).to_be_visible()
        dropdown.click()

    def go_to_profile(self):
        self.open_menu()
        profile = self.page.locator(self.PROFILE_ITEM)
        expect(profile).to_be_visible()
        profile.click()

    def change_avatar(self, filename):
        self.go_to_profile()

        # Verify My Info page
        expect(self.page).to_have_url(re.compile(r"(pim|myInfo)"))

        # Click avatar image
        avatar_icon = self.page.locator(self.AVATAR_ICON)
        expect(avatar_icon).to_be_visible()
        avatar_icon.click()

        # Click change profile picture (+ icon)
        change_icon = self.page.locator(self.CHANGE_ICON)
        expect(change_icon).to_be_visible()
        change_icon.click()

        # Build dynamid path
        root_dir = os.path.dirname(os.path.dirname(__file__))
        image_path = os.path.join(root_dir, "tests", "data", filename)
        image_path = os.path.abspath(image_path)

        if not os.path.exists(image_path):
            raise FileNotFoundError(f"File not found: {image_path}")

        # Upload file
        avatar_input = self.page.locator(self.AVATAR_INPUT)
        avatar_input.wait_for(state="attached", timeout=5000)
        avatar_input.set_input_files(image_path)

        # Click save
        save_btn = self.page.locator(self.SAVE_BUTTON)
        expect(save_btn).to_be_visible()
        save_btn.click()
        self.page.wait_for_load_state("networkidle")


    def logout(self):
        self.open_menu()
        logout_btn = self.page.locator(self.LOGOUT_ITEM)
        expect(logout_btn).to_be_visible()
        with self.page.expect_navigation():
            logout_btn.click()

        # verify back to login page
        expect(self.page).to_have_url(LOGIN_URL)
