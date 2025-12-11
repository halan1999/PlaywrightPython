from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage

def test_login_invalidUser(login_page):
    login_page.open()
    login_page.login_with_invalidUser()
   
def test_login_valid(login_page):
    login_page.open()
    login_page.login_valid_user
    
   
    

    

    
   

    
 



