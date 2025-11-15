import time

import pytest
from playwright.sync_api import Page, expect

from core.base_page import BasePage

class LoginPage(BasePage):
    XPATH_AUTH_CONTENT = '//div[@class="auth-content"]'
    XPATH_IPT_USERNAME = '//input[@id="iusername"]'
    XPATH_IPT_PASSWORD = '//input[@id="ipassword"]'
    XPATH_BTN_LOGIN = '//button[@type="submit"]'

    def __init__(self, page: Page, base_url : str):
        super().__init__(page)
        self.base_url = base_url
        self.__message_error = ''
    
    @property
    def get_message_error(self):
        """Getter"""
        return self.__message_error

    def login(self, username : str, password : str):
        self._goToURL(self.base_url)
        self.verify_page_visible()
        self._take_screenshot('navigate_url.png')
        
        self._setText(self.XPATH_IPT_USERNAME, username)
        self._setText(self.XPATH_IPT_PASSWORD, password)
        self._click(self.XPATH_BTN_LOGIN)

    def verify_page_visible(self):
        locator_auth_content = self.page.locator(self.XPATH_AUTH_CONTENT)
        expect(locator_auth_content).to_be_visible()

    def verify_login_pass(self, username : str):
        label_username = self.page.locator('//a[@href="https://hrm.anhtester.com/erp/my-profile"]//p')
        expect(label_username).to_contain_text(username)
        self._take_screenshot('login_successfully.png')

    def verify_login_fail(self):
        error_component = self.page.locator('//div[contains(@class,"toast-error")]')
        expect(error_component).to_be_visible()
        self._take_screenshot('login_failed.png')

        error_message_element = self.page.locator('//div[contains(@class,"toast-error")]//div[@class="toast-message"]')
        self.__message_error = error_message_element.inner_text()