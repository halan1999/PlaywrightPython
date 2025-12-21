from pages.OrangeHRM.Menu.profile_page import ProfilePage
from core.base_page import BasePage
from playwright.sync_api import Page, expect
from component.header_component import HeaderComponent
from component.menu_component import MenuComponent

class HRM_DashboardPage(BasePage):

    HEADER_TITLE = "//h6"
    TEXT_UNDER_AVATAR = "(//span[contains(text(), 'OrangeHRM')])[2]"
    ICON = "//a[@href='/']"
    URL = "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"

    def __init__(self, page:Page):
        super().__init__(page)  
        self.header_component = HeaderComponent(page)
        self.menu_component = MenuComponent(page)

    def get_title_text(self) -> str:
        return self.page.title()
    
    def logout(self):
        self.header_component.logout()  
        self.page.wait_for_url("**/auth/login")
        self.page.wait_for_load_state(state="networkidle")
        
    def navigate_to_profile(self):
        self.menu_component._click(self.menu_component.XpathMenu.MY_INFO.value)
        self.page.wait_for_load_state(state="networkidle")
        self._take_screenshot("profile_page.png")
        return ProfilePage(self.page)
        
        
