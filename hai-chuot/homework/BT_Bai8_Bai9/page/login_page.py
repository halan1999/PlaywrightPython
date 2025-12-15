from playwright.sync_api import Page, expect
from core.base_page import BasePage

class LoginPage(BasePage):
    XPATH_ORANGE_HRM_LOGIN_LAYOUT = '//div[@class="orangehrm-login-layout"]'
    XPATH_IPT_USERNAME = '//input[@name="username"]'
    XPATH_IPT_PASSWORD = '//input[@name="password"]'
    XPATH_BTN_LOGIN = '//button[@type="submit"]'

    def __init__(self, page: Page, base_url : str):
        super().__init__(page)
        self.base_url = base_url
    
    def login(self, username : str, password : str):
        self._goToURL(self.base_url) 
        self._verify_visible(self.XPATH_ORANGE_HRM_LOGIN_LAYOUT)   
        
        self._setText(self.XPATH_IPT_USERNAME, username)
        self._setText(self.XPATH_IPT_PASSWORD, password)
        self._click(self.XPATH_BTN_LOGIN)

    def verify_login_success(self, expected_title_header : str):
        title_header = self.page.locator('//div[contains(@class,"topbar-header-title")]//h6')
        expect(title_header).to_contain_text(expected_title_header)

    def logout_by_button(self):
        xpath_user_dropdown = '//li[contains(@class,"userdropdown")]'
        self._select2(xpath_user_dropdown, "Logout")
        self._verify_visible(self.XPATH_ORANGE_HRM_LOGIN_LAYOUT)