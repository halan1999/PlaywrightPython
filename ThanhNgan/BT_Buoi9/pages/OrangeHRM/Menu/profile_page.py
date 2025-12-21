from core.base_page import BasePage
from playwright.sync_api import Page, expect
from component.header_component import HeaderComponent
from component.menu_component import MenuComponent

class ProfilePage(BasePage):

    AVATAR = "//img[@class='employee-image']"
    AVATAR_INPUT = "//input[@type='file']"
    AVATAR_ICON_BUTTON = "//div[@class='orangehrm-employee-picture']//button" 
    PERSONAL_DETAILS = "//div[@class='orangehrm-edit-employee-content']"
    EMPLOYEE_FIRST_NAME = "//input[@name='firstName']"
    EMPLOYEE_MIDDLE_NAME = "//input[@name='middleName']"
    EMPLOYEE_LAST_NAME = "//input[@name='lastName']"
    EMPLOYEE_ID = "(//input[@class='oxd-input oxd-input--active'])[1]"
    EMPLOYEE_DRIVER_LICENSE = "(//input[@class='oxd-input oxd-input--active'])[3]"
    EMPLOYEE_LICENSE_EXPIRY_DATE = "(//input[@class='oxd-input oxd-input--active'])[4]"

    def __init__(self, page:Page):
        super().__init__(page)  
        self.header_component = HeaderComponent(page)
        self.menu_component = MenuComponent(page)

    def get_employee_fullname(self) -> str:
        first_name = self._get_input_value(self.EMPLOYEE_FIRST_NAME)
        middle_name = self._get_input_value(self.EMPLOYEE_MIDDLE_NAME)
        last_name = self._get_input_value(self.EMPLOYEE_LAST_NAME)
        return f"{first_name} {middle_name} {last_name}".strip()
    
    def update_avatar(self, new_avatar_path: str):
        self._click(self.AVATAR)
        self.page.wait_for_load_state(state="networkidle")
        self._take_screenshot("before_upload_avatar.png")
        self._click(self.AVATAR_ICON_BUTTON)
        self._upload_file(self.AVATAR_INPUT, new_avatar_path)
        

