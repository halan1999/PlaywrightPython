from core.common_locators import CommonLocators
from core.base_page import BasePage

class DataTableComponents(BasePage):
    SEARCH_INPUT = CommonLocators._input_by_attribute_xpath("type", "search")
    TABLE = "//table[@id='xin_table']"
    HEADERS_TABLE = lambda name: f"//thead//th[normalize-space()='{name}']"
    ROWS_TABLE = "//tbody"
    EDIT_ICON = lambda name : f"//td[normalize-space()='{name}']//i[@class='feather icon-edit']"
    DELETE_ICON = lambda name : f"//td[normalize-space()='{name}']//i[@class='feather icon-trash-2']"
    # Pagination Controls
    ROW_PER_PAGE_SELECTOR = "//select[@name='xin_table_length']"
    PREVIOUS_PAGE_BUTTON = "//li[@id='xin_table_previous']"
    NEXT_PAGE_BUTTON = "//li[@id='xin_table_next']"
    PAGINATION_BUTTONS = "//ul[@class='pagination']/li"
    # Popup
    POPUP = "//div[@id='ajax_view_modal']"
    CANCEL_BUTTON_POPUP = "//div[@id='ajax_view_modal']//button[normalize-space()='Close']"
    SUBMIT_BUTTON_POPUP = "//div[@id='ajax_view_modal']//button[@type='submit']"
    
    def __init__(self, page):
        super().__init__(page)
        self.page = page

    def _click_edit_icon(self, record: str):
        self._click(self.EDIT_ICON(record))
        # xác định popup hiển thị
        self._expect_to_be_visible(self.POPUP)

    def _click_delete_icon(self, record: str):
        self._click(self.DELETE_ICON(record))
        # xác định popup hiển thị
        self._expect_to_be_visible(self.POPUP)

    def _click_cancel_button_popup(self):
        self._click(self.CANCEL_BUTTON_POPUP)
        # xác định popup đã ẩn
        self._expect_to_be_hidden(self.POPUP)

    def _click_submit_button_popup(self):
        self._click(self.SUBMIT_BUTTON_POPUP)
        # xác định popup đã ẩn
        self._expect_to_be_hidden(self.POPUP)

    def _click_column_table(self, col_name: str):
        self._click(self.HEADERS_TABLE(col_name))

    