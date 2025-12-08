import json
from ...core.base_page import BasePage
from playwright.sync_api import expect

class HeaderComponent(BasePage):
    account_setting = "//a[@data-original-title='Account Settings']"
    apps = "//span[normalize-space(.)='Apps']"
    system_calendar = "//a[@data-original-title = 'System Calendar'])"
    system_report = "//a[@data-original-title = 'System Reports']"
    language = "//a[@data-toggle= 'dropdown']//img[contains(@src, 'languages')]"
    todo_list = "//a[@data-original-title='Todo List']"
    user_avtar = "//img[@class='user-avtar']"
    logout_list = "//span[normalize-space(.)='Logout']"

    def __init__(self, page):
        super().__init__(page)    
        
    