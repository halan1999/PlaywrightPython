from buoi8.pages.base_page import BasePage


class LinkedlnPage(BasePage):

    def __init__(self, page):
        super().__init__(page)

    LINKEDLN_NAME = "//h1[@id='ember35']"

    def assert_visible_linkedln_name(self):
        linkedln_name = self.get_url()
        assert linkedln_name == "https://www.linkedin.com/company/orangehrm"