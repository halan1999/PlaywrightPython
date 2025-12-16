from enum import Enum

from core.base_component import BaseComponent
from core.base_page import BasePage

class XpathHeader(Enum):
    """
    XPath của tất cả các icons trên thanh Header của Chương trình
    """
    ACCOUNT_SETTING = '//a[@data-original-title="Account Settings"]'    
    SYSTEM_CALENDAR = '//a[@data-original-title="System Calendar"]'
    SYSTEM_REPORT = '//a[@data-original-title="System Reports"]'
    TODO_LIST = '//a[@data-original-title="Todo List"]'
    PROFILE_ACCOUNT = '//img[@class="user-avtar"]/parent::a'
    APPS = '//span[@data-original-title="Apps"]/parent::a'

class HeaderComponent(BaseComponent, BasePage):    
    def click_single_header(self, xpath_header : XpathHeader):
        """
        Thực hiện click vào các icon đơn lẻ trên header
        """
        self._click(xpath_header.value)

    def click_header_dropdown(self, xpath_header : XpathHeader, label_dropdown_item : str):
        """
        Thực hiện click vào các icon có dạng dropdown list trên header
        """
        xpath_dropdown_item = f'// div[contains(@class,"dropdown-menu")]//span[normalize-space()="{label_dropdown_item}"]/parent::a'
        self._click_two_component(xpath_header.value, xpath_dropdown_item)