from core.base_component import BaseComponent

class MenuComponent(BaseComponent):
    def click_single_menu(self, label_menu : str):
        xpath_menu = f'//span[normalize-space()="{label_menu}"]/parent::a'
        self._click_single_component(xpath_menu)

    def click_menu(self, label_menu : str, label_sub_menu : str):
        xpath_menu = f'//a[normalize-space()="{label_menu}"]'
        xpath_sub_menu = f'{xpath_menu}/following-sibling::ul//a[normalize-space()="{label_sub_menu}"]'
        self._click(xpath_menu, xpath_sub_menu)