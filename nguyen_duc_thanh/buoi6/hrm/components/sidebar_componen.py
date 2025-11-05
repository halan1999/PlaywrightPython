from buoi5.hrm.pages.base_page import BasePage


class SizeBarComponent(BasePage):
    DISCIPLINARY_CASES = "//span[normalize-space()='Disciplinary Cases']"

    def scroll_to_end(self):
        self.get_locator(self.DISCIPLINARY_CASES).scroll_into_view_if_needed()
        self.take_screenshot("scroll_to_end_sizebar.png")
