from core.common_locators import CommonLocators
from core.base_page import BasePage
from components.toast_message_components import ToastMessageComponents
from components.popup_components import PopupComponents

class DataTableComponents(BasePage):
    SEARCH_INPUT = CommonLocators._input_by_attribute_xpath("type", "search")
    TABLE = "//table[@id='xin_table']"
    HEADERS_TABLE = lambda name: f"//thead//th[normalize-space()='{name}']"
    ROWS_TABLE = "//tbody/tr"
    NO_DATA_ROW_TABLE = "//tbody/tr[normalize-space()='No records available']"
    # Pagination Controls
    ROW_PER_PAGE_SELECTOR = "//select[@name='xin_table_length']"
    PREVIOUS_PAGE_BUTTON = "//li[@id='xin_table_previous']"
    NEXT_PAGE_BUTTON = "//li[@id='xin_table_next']"
    PAGINATION_BUTTONS = "//ul[@class='pagination']/li"
    ELLIPSIS_BUTTONS = "//li[@id='xin_table_ellipsis']"
    # Popup
    EDIT_POPUP = "//div[@id='ajax_view_modal']"
    DELETE_POPUP = "//form[@id='delete_record']"

    def EDIT_ICON(self, name):
        return f"//td[normalize-space()='{name}']//i[@class='feather icon-edit']"

    def DELETE_ICON(self, name):
        return f"//td[normalize-space()='{name}']//i[@class='feather icon-trash-2']"
    
    def BUTTON_PAGINATION_CONTROLS(self, name_button):
        return f"//ul[@class='pagination']/li/a[normalize-space()='{name_button}']"

    def __init__(self, page):
        super().__init__(page)
        self.page = page
        self.toast = ToastMessageComponents(page)
        self.popup = PopupComponents(page)

    # region action table
    def _click_edit_icon(self, record: str):
        self._click(self.EDIT_ICON(record))
        # xác định popup hiển thị
        self._expect_to_be_visible(self.EDIT_POPUP)

    def _click_delete_icon(self, record: str):
        self._click(self.DELETE_ICON(record))
        # xác định popup hiển thị
        self._expect_to_be_visible(self.DELETE_POPUP)

    def _click_column_table(self, col_name: str):
        self._click(self.HEADERS_TABLE(col_name))

    def _delete_record(self, record: str, confirm: bool=True):
        """
        THực hiện search record
        click icon delete
        nếu confirm = true => nhấn ok thực hiện xóa
        ngược lại đóng popup xóa
        """
        self._search_with_result(record)
        self._click_delete_icon(record)
        self.popup._confirm_delete_record(confirm=confirm)
        if confirm:
            self._search_with_no_result(record)
        else:
            self._search_with_result(record)

    def _perform_sort_column(self):
        pass
    
    # endregion

    # region function search
    def _perform_search(self, keyword: str):
        self._fill(self.SEARCH_INPUT, keyword)

    def _search_with_no_result(self, keyword: str):
        self._perform_search(keyword)
        self._expect_to_be_visible(self.NO_DATA_ROW_TABLE)

    def _search_with_result(self, keyword: str):
        self._perform_search(keyword)
        self._expect_to_be_hidden(self.NO_DATA_ROW_TABLE)
    # endregion

    # region Pagination Controls
    def _select_row_per_page(self, table_length: str = None):
        """
        table_length: gồm giá trị mặc định là 10 25 50 100
        """
        try:
            self._select_option(self.ROW_PER_PAGE_SELECTOR, value=table_length)
            rows_count = self._get_locator(self.ROWS_TABLE).count()
            assert rows_count <= int(table_length)
        except ValueError:
            print(f"Locator {self.ROW_PER_PAGE_SELECTOR} không tồn tại value: {table_length}")
        
    def _click_button_in_pagination_controls(self, name_button):
        """
        Format: Previous 1 2 3 ... 6 7 Next
        """
        try:
            self._click(self.BUTTON_PAGINATION_CONTROLS(name_button))
        except ValueError:
            print(f"Không tồn tại locator: {self.BUTTON_PAGINATION_CONTROLS(name_button)}") 
    # endregion
