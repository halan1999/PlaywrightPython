from playwright.sync_api import Page, expect
from pages.base_page import BasePage

class HomePage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.MENUS = {
            "Home": "Home",
            "Projects": "Projects",
            "Tasks": "Tasks"
        }

        self._profile_link = "//a[contains(@href,'my-profile')]//p"
        self._left_menu = '//span[normalize-space()="%s"]'
        self._log_out_button = '//div[@class="page-header"]//a[normalize-space()="Logout"]'

    def is_loaded(self):
        expect(self.page.locator(self._profile_link)).to_be_visible(timeout=5000)
        return True
    
    def is_project_menu_visible(self) -> bool:
        menu_locator = self._left_menu % self.MENUS["Projects"]
        expect(self.page.locator(menu_locator)).to_be_visible(timeout=5000)
        return True

    def is_tasks_menu_visible(self) -> bool:
        menu_locator = self._left_menu % self.MENUS["Tasks"]
        expect(self.page.locator(menu_locator)).to_be_visible(timeout=5000)
        return True

    
    def click_menu_item(self, menu_name: str):
        menu_locator = self._left_menu % menu_name
        expect(self.page.locator(menu_locator)).to_be_visible(timeout=5000)
        self.page.locator(menu_locator).click()
        return self
                        

    def is_logout_button_visible(self):
        expect(self.page.locator(self._log_out_button)).to_be_visible(timeout=5000)
        return self
    
    def logout(self):
        self.page.locator(self._log_out_button).click()