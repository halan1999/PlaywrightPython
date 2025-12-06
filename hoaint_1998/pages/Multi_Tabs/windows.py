from core.base_page import BasePage
from core.common_locators import CommonLocators
from pages.Multi_Tabs.new_windows import NewWindows

class Windows(BasePage):
    CLICK_HERE_LINK = CommonLocators._normalize_space_xpath("a", "Click Here")
    URL = "https://the-internet.herokuapp.com/windows"

    def __init__(self, page):
        super().__init__(page)
        self.page = page

    def _go_to_windows(self):
        self._goto(self.URL)

    def open_new_window(self, timeout = 15000) -> NewWindows:
        with self.page.context.expect_page(timeout=timeout) as new_page_info:
            self._click(self.CLICK_HERE_LINK)
        new_page = new_page_info.value
        new_page.wait_for_load_state("load")
        return NewWindows(new_page)

    