import allure
import pytest
from pages.saucedemo.login_page import LoginPage
from pages.saucedemo.product_page import ProductPage


@allure.title("Login successfully with valid user")
@allure.description(
    "Verify that standard user can login successfully "
    "and product page is displayed"
)
def test_login_standard_user(page, credentials):
    login = LoginPage(page)
    product = ProductPage(page)

    user = next(u for u in credentials if u["username"] == "standard_user")

    with allure.step("Open login page"):
        login.open()

    with allure.step(f"Login with user: {user['username']}"):
        login.login(user["username"], user["password"])

    with allure.step("Verify product page is loaded"):
        assert product.is_product_page_loaded()


@allure.title("Login failed with invalid user")
@allure.description(
    "Verify that locked out user cannot login "
    "and error message is displayed"
)

def test_login_locked_out_user(page, credentials):
    login = LoginPage(page)

    user = next(u for u in credentials if u["username"] == "locked_out_user")

    with allure.step("Open login page"):
        login.open()

    with allure.step(f"Login with user: {user['username']}"):
        login.login(user["username"], user["password"])

    with allure.step("Verify error message is shown"):
        assert login.is_login_failed()
