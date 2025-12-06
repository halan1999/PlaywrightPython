from locators.core_hr.department.department_locators import DepartmentLocator as DL
from components.data_table_components import DataTableComponents
from components.toast_message_components import ToastMessageComponents
from core.base_page import BasePage
from utils.messages import SUCCESS_MESSAGE, ERROR_MESSAGE

class Department(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.data_table = DataTableComponents(page)
        self.toast_message = ToastMessageComponents(page)

    def _create_department(self, value: str):
        self._enter_department_name(value)
        self._click_submit_button()
        self.toast_message._expect_display_message(SUCCESS_MESSAGE["COMMON"]["CREATE_SUCCESS"])
    
    def _enter_department_name(self, value: str):
        self._fill(DL.NAME_INPUT, value)

    def _click_submit_button(self):
        self._click(DL.SAVE_BUTTON)

    