
from playwright.sync_api import expect
import pytest
from buoi5.pages.login_page import LoginPage


def test_successful_login_standard_user(page):
    login_page = LoginPage(page)
    login_page.login("standard_user", "secret_sauce")
    login_page.assert_login_successful()

def test_login_failure_locked_user(page):
    login_page = LoginPage(page)
    login_page.login("locked_out_user", "secret_sauce")
    login_page.assert_error_message_visible(
        "Epic sadface: Sorry, this user has been locked out."
    )

