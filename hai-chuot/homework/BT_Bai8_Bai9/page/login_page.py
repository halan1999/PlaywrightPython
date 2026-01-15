from enum import Enum

from playwright.sync_api import Page, expect
from core.base_page import BasePage

class LinkFooter(Enum):
    """
    Links to related pages in the footer
    """
    LINKEDIN = 'https://www.linkedin.com/company/orangehrm/mycompany/'    
    FACEBOOK = 'https://www.facebook.com/OrangeHRM/'
    TWITTER = 'https://twitter.com/orangehrm?lang=en'
    YOUTUBE = 'https://www.youtube.com/c/OrangeHRMInc'

class LoginPage(BasePage):
    XPATH_ORANGE_HRM_LOGIN_LAYOUT = '//div[@class="orangehrm-login-layout"]'
    XPATH_IPT_USERNAME = '//input[@name="username"]'
    XPATH_IPT_PASSWORD = '//input[@name="password"]'
    XPATH_BTN_LOGIN = '//button[@type="submit"]'

    def __init__(self, page: Page, base_url : str):
        super().__init__(page)
        self._goToURL(base_url) 
        self._verify_visible(self.XPATH_ORANGE_HRM_LOGIN_LAYOUT)  
    
    def login(self, username : str, password : str):        
        self._setText(self.XPATH_IPT_USERNAME, username)
        self._setText(self.XPATH_IPT_PASSWORD, password)
        self._click(self.XPATH_BTN_LOGIN)

    def verify_login_success(self, expected_title_header : str):
        title_header = self.page.locator('//div[contains(@class,"topbar-header-title")]//h6')
        expect(title_header).to_contain_text(expected_title_header)

    def logout(self):
        xpath_user_dropdown = '//li[contains(@class,"userdropdown")]'
        self._select2(xpath_user_dropdown, "Logout")
        self._verify_visible(self.XPATH_ORANGE_HRM_LOGIN_LAYOUT)

    def open_related_page(self, link_footer: LinkFooter) -> Page:
        xpath_icon = f'//a[@href="{link_footer.value}"]'

        with self.page.context.expect_page() as new_page:
            self._click(xpath_icon)

        opened_page = new_page.value
        opened_page.wait_for_load_state()

        return opened_page
    
    def back_to_login_page(self):
        self.page.bring_to_front()