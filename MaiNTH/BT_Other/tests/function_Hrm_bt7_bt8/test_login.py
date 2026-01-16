
from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage
import pytest


@pytest.mark.usefixtures("open_login_page")
def test_login_invalidUser(login_page):
    # login_page.open()
    login_page.login_with_invalidUser()

@pytest.mark.usefixtures("open_login_page")
def test_login_blankUser(login_page):
    # login_page.open()
    login_page.login_with_blankUser()

@pytest.mark.usefixtures("open_login_page")
def test_login_valid(login_page):
    # login_page.open()
    login_page.login_valid_user()



   

    
   
    

    

    
   

    
 


