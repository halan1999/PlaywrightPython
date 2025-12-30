from core.base_page import BasePage
from core.common_locators import CommonLocators

class NewWindows(BasePage):
    NEW_WINDOW_LABLE = "//h3"

    def __init__(self, page):
        super().__init__(page)
        self.page = page

    def _verify_page(self):
        assert self._inner_text(self.NEW_WINDOW_LABLE) == "New Window", "Khong phai page: new window"