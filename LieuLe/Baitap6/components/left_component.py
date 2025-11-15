import json
from ..core.base_page import BasePage
from playwright.sync_api import expect

class LeftComponent(BasePage):
    home = "//span[normalize-space(text())='Home']"
    attendance = "//span[normalize-space(.) = 'Attendance']"
    projects = "//span[normalize-space(.) = 'Projects']"
    tasks = "//span[normalize-space(.) = 'Tasks']"
    payroll = "//span[normalize-space(.) = 'Payroll']"
    requests = "//a[normalize-space(.) = 'Requests']"
    helpdesk = "//span[normalize-space(.) = 'Helpdesk']"
    training_sessions = "//span[normalize-space(.) = 'Training Sessions']"
    left_menu1 = "//div[@class ='navbar-content ps ps--active-y']"
    
    def __init__(self, page):
        super().__init__(page)    
        
    