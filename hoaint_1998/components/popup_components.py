from core.common_locators import CommonLocators
from core.base_page import BasePage

class PopupComponents(BasePage):
    # Popup
    POPUP = "//div[@id='ajax_view_modal']"
    CANCEL_BUTTON = "//div[@id='ajax_view_modal']//button[normalize-space()='Close']"
    SUBMIT_BUTTON = "//div[@id='ajax_view_modal']//button[@type='submit']"

    def __init__(self, page):
        super().__init__(page)
        self.page = page

    def _click_cancel_button_popup(self):
        self._click(self.CANCEL_BUTTON)
        # xác định popup đã ẩn
        self._expect_to_be_hidden(self.POPUP)

    def _click_submit_button_popup(self):
        self._click(self.SUBMIT_BUTTON)
        # xác định popup đã ẩn
        self._expect_to_be_hidden(self.POPUP)

    def _confirm_delete_record(self, confirm: bool = True):
        if confirm:
            self._click_submit_button_popup()
        else:
            self._click_cancel_button_popup()