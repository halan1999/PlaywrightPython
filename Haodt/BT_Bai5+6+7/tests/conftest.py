import pytest
from playwright.sync_api import Playwright
from pages.login_page import LoginPage

#1. Page Object: LoginPage
@pytest.fixture
def login_page(page):
    return LoginPage(page)

#2. Fixture thuc hien login (optional neu can login san)\
@pytest.fixture
def logged_in_page(login_page):
    login_page.open()
    login_page.login_valid_user()
    
    login_page.header.wait_for_user_logged_in()

    return login_page
#Class scope
@pytest.fixture(scope="class")
def logged_in_class(request,browser):
    context=browser.new_context()
    page= context.new_page()

    #login 1 lan cho ca class
    lp=LoginPage(page)
    lp.open()
    lp.login_valid_user()
    #lp.header.wait_for_user_logged_in()

    #Gan vao class
    request.cls.page=page
    request.cls.login_page=lp
    request.cls.context=context

    yield

    #Teardown khi class chay xong

    context.close()

#Module scope
@pytest.fixture(scope="module")
def logged_in_module(brower):
    context=brower.new_context()
    page=context.new_page()

    lp=LoginPage(page)
    lp.open()
    lp.login_valid_user()
    lp.header.wait_for_user_logged_in()

    yield page, lp