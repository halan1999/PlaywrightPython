from playwright.sync_api import Locator
from locators.core_hr.designation.designation_locators import DesignationLocators as DL
from core.base_page import BasePage
from components.data_table_components import DataTableComponents
from components.toast_message_components import ToastMessageComponents
from components.popup_components import PopupComponents
from components.menu_bar_components import MenuBarComponents
from utils.data_factory import _get_random_test
from faker import Faker

class Designation(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.table = DataTableComponents(page)
        self.toast = ToastMessageComponents(page)
        self.menu = MenuBarComponents(page)
        self.popup = PopupComponents(page)
        self.faker = Faker()

    def _go_to_core_hr_designation(self):
        self.menu._click_sub_menu("Core HR", "Designation")

    def _go_to_designation_at_tab_bar(self):
        self._click(DL.DESIGNATION_TAB)

    def _create_designation(self, department_name: str, designation_name: str = None, description: str = None):
        self._perform_create_designation(department_name, designation_name, description)
        self._click(DL.SAVE_BUTTON)
        self.toast._expect_display_created_message()

    def _edit_designation(self, record: str, department_name: str=None, designation_name: str = None, description: str = None):
        self.table._search_with_result(record)
        self.table._click_edit_icon(record)
        self._perform_edit_designation(department_name, designation_name, description)
        self.popup._click_submit_button_popup()

    def _delete_designation(self, record : str, confirm : bool=True):
        self.table._delete_record(record, confirm)

    def _perform_create_designation(self, department_name: str = None, designation_name: str = None, description: str = None):
        designation_name_value = designation_name or f"designation_{_get_random_test()}"
        description_value = description or self.faker.sentence()
        self._fill(DL.DESIGNATION_NAME_INPUT, designation_name_value)
        self._fill(DL.DESCRIPTION_TEXTAREA, description_value)
        self._click(DL.DEPARTMENT_SELECTBOX)
        self._enhanced_select(department_name)
        self.last_designation_name = designation_name_value

    def _perform_edit_designation(self, department_name: str = None, designation_name: str = None, description: str = None):
        if designation_name is not None:
            self._fill(f"{self.popup.EDIT_POPUP}{DL.DESIGNATION_NAME_INPUT}", designation_name)
            self.last_designation_name = designation_name
        if description is not None:
            self._fill(f"{self.popup.EDIT_POPUP}{DL.DESCRIPTION_TEXTAREA}", description)
        if department_name is not None:
            self._click(f"{self.popup.EDIT_POPUP}{DL.DEPARTMENT_SELECTBOX}")
            self._enhanced_select(department_name)
        
    
    def _enhanced_select(self, department_name: str, confirm: bool = True):
        """
        Nhập giá trị tìm kiếm trong combobox
        nếu confirm = True => expect hiển thị kết quả chính xác với keyword
        ngược lại là ko tìm thấy
        """
        self._expect_to_be_visible(DL.DEPARTMENT_INPUT)
        self._fill(DL.DEPARTMENT_INPUT, department_name)
        if confirm:
            expect_result_locator = DL.DEPARTMENT_ITEM_IN_LIST(department_name)
            self._expect_to_be_visible(expect_result_locator)
            self._click(expect_result_locator)
            self._expect_to_be_hidden(DL.DEPARTMENT_INPUT)
        else:
            expect_result_locator = DL.DEPARTMENT_ITEM_IN_LIST("No results found")
            # đóng combobox
            self.page.keyboard.press("Escape")
    
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
