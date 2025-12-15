
from components.header_component import HeaderComponent, XpathHeader
from components.menu_component import MenuComponent
from core.base_page import BasePage

class HomePage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.header = HeaderComponent(page)
        self.menu = MenuComponent(page)

    def click_header_function(self, xpath_header : XpathHeader):
        self.header.click_single_header(xpath_header)
    
    def click_apps_header_function(self, label_dropdown_item : str):
        self.header.click_header_dropdown(XpathHeader.APPS, label_dropdown_item)

    def click_menu_function(self, label_menu : str):
        self.menu.click_single_menu(label_menu)

    def click_sub_menu_function(self, label_menu : str, label_sub_menu : str):
        self.menu.click_menu(label_menu, label_sub_menu)

     