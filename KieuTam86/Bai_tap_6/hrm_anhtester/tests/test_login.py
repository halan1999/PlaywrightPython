from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from components.header_component import HeaderComponent
from playwright.sync_api import expect
import time, json


def test_login(page):
    login_page = LoginPage(page)
    print("Test login success")
    login_page.login_success()

def test_Account_Setting(page):
    test_login(page)
    header = HeaderComponent(page)
    header.navigate_Acc_Setting()

def test_Choose_Apps(page):
    test_login(page)
    header = HeaderComponent(page)
    header.choose_Apps()

def test_System_Calendar(page):
    test_login(page)
    header = HeaderComponent(page)
    header.navigate_System_Calendar()

def test_SysTem_Reports(page):
    test_login(page)
    header = HeaderComponent(page)
    header.navigate_System_Reports()

def test_Choose_Language(page):
    test_login(page)
    header = HeaderComponent(page)
    header.choose_Language()

def test_ToDoList(page):
    test_login(page)
    header = HeaderComponent(page)
    header.navigate_ToDoList()    

def test_logout(page):
    test_login(page)
    header = HeaderComponent(page)
    header.logout_by_button()
    print("Test logout success")

