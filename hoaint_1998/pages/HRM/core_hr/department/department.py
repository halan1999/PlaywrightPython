from locators.core_hr.department.department_locators import DepartmentLocator as DL
from components.data_table_components import DataTableComponents
from components.toast_message_components import ToastMessageComponents
from components.popup_components import PopupComponents
from components.menu_bar_components import MenuBarComponents
from core.base_page import BasePage
from utils.data_factory import _get_random_test

class Department(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.table = DataTableComponents(page)
        self.toast = ToastMessageComponents(page)
        self.menu = MenuBarComponents(page)
        self.popup = PopupComponents(page)

    def _go_to_core_hr_deparment(self):
        self.menu._click_sub_menu(parent="Core HR", child="Department")

    def _create_department(self, value: str = None): 
        self._enter_department_name(value)
        self._click_submit_button()
        self.toast._expect_display_created_message()

    def _edit_department(self, record: str, value: str = None):
        self.table._search_with_result(record)
        self.table._click_edit_icon(record)
        self._perform_update_department(value)
        self.popup._click_submit_button_popup()

    def _delete_department(self, record: str, confirm: bool=True):
        self.table._delete_record(record, confirm)
    
    def _enter_department_name(self, value: str = None):
        self.last_record_name = value or _get_random_test()
        self._fill(DL.NAME_INPUT, self.last_record_name)

    def _click_submit_button(self):
        self._click(DL.SAVE_BUTTON)

    def _perform_update_department(self, value: str = None):
        self.last_record_name = value or _get_random_test()
        self._fill(DL.NAME_INPUT_EDIT_POPUP, self.last_record_name)

    def _select_row_per_page(self, table_length: str):
        """
        table_length: gồm giá trị mặc định là 10 25 50 100
        """
        self.table._select_row_per_page(table_length=table_length)

    def _click_button_in_pagination_controls(self, name_button):
        """
        Format: Previous 1 2 3 ... 6 7 Next
        """
        self.table._click_button_in_pagination_controls(name_button)
    