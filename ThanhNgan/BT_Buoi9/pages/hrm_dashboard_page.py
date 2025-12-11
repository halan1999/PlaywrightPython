from core.base_page import BasePage
from playwright.sync_api import Page, expect
from component.header_component import HeaderComponent

class HRM_DashboardPage(BasePage):

    HEADER_TITLE = "//h6"
    TEXT_UNDER_AVATAR = "(//span[contains(text(), 'OrangeHRM')])[2]"
    ICON = "//a[@href='/']"
    URL = "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"

    def __init__(self, page:Page):
        super().__init__(page)  
        self.header_component = HeaderComponent(page)

    def get_title_text(self) -> str:
        return self.page.title()
    
    def logout(self):
        self.header_component.logout()  
        self.page.wait_for_url("**/auth/login")
        self.page.wait_for_load_state()
        
        
        
