import pytest
from buoi9.pages.login_page import LoginPage

@pytest.fixture
def login_page(page):
    return LoginPage(page)


@pytest.fixture
def logged_page(page):
    login = LoginPage(page)
    login.go_to_loginpage()
    cred = login.get_credential()

    dashboard_page = login.login(
        cred["valid_user"]["username"],
        cred["valid_user"]["password"]
    )
    return dashboard_page
# @pytest.fixture
# def login_page(page):
#     lp = LoginPage(page)
#     lp.go_to_loginpage()
#     return lp

# @pytest.fixture
# def logged_page(login_page):
#     cred = login_page.get_credential()
#     dashboard_page = login_page.login(
#         cred["valid_user"]["username"],
#         cred["valid_user"]["password"]
#     )
#     return dashboard_page
