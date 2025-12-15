from core.base_component import BaseComponent
from core.base_page import BasePage

class MenuComponent(BaseComponent, BasePage):
    def click_single_menu(self, label_menu : str):
        xpath_menu = f'//span[normalize-space()="{label_menu}"]/parent::a'
        self._click(xpath_menu)

    def click_menu(self, label_menu : str, label_sub_menu : str):
        xpath_menu = f'//a[normalize-space()="{label_menu}"]'
        xpath_sub_menu = f'{xpath_menu}/following-sibling::ul//a[normalize-space()="{label_sub_menu}"]'
        self._click_two_component(xpath_menu, xpath_sub_menu)