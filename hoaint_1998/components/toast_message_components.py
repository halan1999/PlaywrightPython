from core.common_locators import CommonLocators
from utils.messages import SUCCESS_MESSAGE, ERROR_MESSAGE
from core.base_page import BasePage

class ToastMessageComponents(BasePage):
    CREATE_MESSAGE = f"{CommonLocators._contains_text_xpath("div", SUCCESS_MESSAGE["COMMON"]["CREATE_SUCCESS"])}/ancestor::div[@id='toast-container']"
    UPDATE_MESSAGE = f"{CommonLocators._contains_text_xpath("div", SUCCESS_MESSAGE["COMMON"]["UPDATE_SUCCESS"])}/ancestor::div[@id='toast-container']"
    DELETE_MESSAGE = f"{CommonLocators._contains_text_xpath("div", SUCCESS_MESSAGE["COMMON"]["DELETE_SUCCESS"])}/ancestor::div[@id='toast-container']"
    XPATH_MESSAGE = lambda message: f"//div[contains(text(), '{message}')]/ancestor::div[@id='toast-container']"

    def __init__(self, page):
        super().__init__(page)
        self.page = page

    def _expect_display_message(self, message: str):
        """
        message: nhập 1 phần nội dung message
        """
        self._expect_to_be_visible(self.XPATH_MESSAGE(message))
