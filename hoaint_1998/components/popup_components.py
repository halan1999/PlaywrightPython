from core.common_locators import CommonLocators
from core.base_page import BasePage

class PopupComponents(BasePage):
    # Popup
    EDIT_POPUP = "//div[@id='ajax_view_modal']"
    DELETE_POPUP = "//form[@id='delete_record']"

    def CANCEL_BUTTON(self, popup_name: str = "edit"):
        xpath_cancel_button = "//button[normalize-space()='Close']"
        if popup_name == "edit":
            return f"{self.EDIT_POPUP}{xpath_cancel_button}"
        else:
            return f"{self.DELETE_POPUP}{xpath_cancel_button}"
        
    def SUBMIT_BUTTON(self, popup_name: str = "edit"):
        xpath_submit_button = "//button[@type='submit']"
        if popup_name == "edit":
            return f"{self.EDIT_POPUP}{xpath_submit_button}"
        else:
            return f"{self.DELETE_POPUP}{xpath_submit_button}"

    def __init__(self, page):
        super().__init__(page)
        self.page = page

    def _click_cancel_button_popup(self, popup_name: str = "edit"):
        self._click(self.CANCEL_BUTTON(popup_name=popup_name))
        # xác định popup đã ẩn
        if popup_name == "edit":
            self._expect_to_be_hidden(self.EDIT_POPUP)
        else:
            self._expect_to_be_hidden(self.EDIT_POPUP)

    def _click_submit_button_popup(self, popup_name: str = "edit"):
        self._click(self.SUBMIT_BUTTON(popup_name=popup_name))
        # xác định popup đã ẩn
        if popup_name == "edit":
            self._expect_to_be_hidden(self.EDIT_POPUP)
        else:
            self._expect_to_be_hidden(self.EDIT_POPUP)


    def _confirm_delete_record(self, confirm: bool = True, popup_name: str = "delete"):
        if confirm:
            self._click_submit_button_popup(popup_name)
        else:
            self._click_cancel_button_popup(popup_name)