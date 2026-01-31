from playwright.sync_api import Page, expect
from Core.Base_page import BasePage
from Core.config import NEW_TAB_URL

class NewTabWindowsPage(BasePage):
    #selector:
    HEADING="h3"
    CLICK_HERE_LINK="a[href='/windows/new']"

    def __init__(self, page:Page, url:str):
        super().__init__(page)
        self.url=url
    def open(self)-> None:
        self.goto(self.url)
    def assert_heading(self, text:str) -> None:
        expect(self.page.locator(self.HEADING)).to_have_text(text)
    def open_new_tab(self)->Page:
        with self.page.expect_popup() as popup_info:
            self.page.locator(self.CLICK_HERE_LINK).click()
            return popup_info.value


 