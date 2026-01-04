from playwright.sync_api import expect
from pages.base_page import BasePage

class LeftMenu(BasePage):
    # Locators
    _dashboard_item = '//span[text()="Dashboard"]/ancestor::li'
    _user_item = '//span[text()="User"]/ancestor::li'
    _book_item = '//span[text()="Book"]/ancestor::li'
    _promotion_item = '//span[text()="Promotion"]/ancestor::li'
    _file_item = '//span[text()="File"]/ancestor::li'
    _database_item = '//span[text()="Database"]/ancestor::li'

    def __init__(self, page):
        super().__init__(page)

        self._left_menu_items = [
            self._dashboard_item,
            self._user_item,
            self._book_item,
            self._promotion_item,
            self._file_item,
            self._database_item,
        ]

    def is_left_menu_visible(self, timeout: int = 5000):
        for item in self._left_menu_items:
            expect(self.page.locator(item)).to_be_visible(timeout=timeout)
        return True