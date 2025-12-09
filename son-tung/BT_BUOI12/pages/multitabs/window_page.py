from BT_BUOI12.core.base_page import BasePage
from BT_BUOI12.pages.multitabs.new_social_page import NewWindowPage
from playwright.sync_api import Page

class WindowPage(BasePage):
    URL = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    heading = "h5"
    click_linkedin = "//div[@class='orangehrm-login-footer-sm']//a[1]"
    click_facebook = "//div[@class='orangehrm-login-footer-sm']//a[2]"
    click_twitter = "//div[@class='orangehrm-login-footer-sm']//a[3]"
    click_youtube = "//div[@class='orangehrm-login-footer-sm']//a[4]"

    def __init__(self, page):
        super().__init__(page)

    def open_url(self):
        self._visit(self.URL)

    def get_heading_text(self) -> str:
        return self._get_text(self.heading)

    def open_new_tab_and_return_page_object(self, button_page) -> NewWindowPage:
        # Click link để mở tab mới và trả về NewWindowPage POM của tab mới
        with self.page.context.expect_page() as new_page_info:
            self._click(button_page)

        new_page = new_page_info.value
        new_page.wait_for_load_state()

        # Trả về POM cho tab mới
        return NewWindowPage(new_page)