from core.base_page import BasePage
from core.common_locators import CommonLocators as CL
from playwright.sync_api import Page
from pages.Multi_Tabs.twitter_organge import TwitterOrange

class Orange_Hrm_Login(BasePage):
    URL = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    USER_NAME_BUTTON = CL._input_by_attribute_xpath("name", "username")
    PASSWORD_BUTTON = CL._input_by_attribute_xpath("name", "password")
    SUBMIT_BUTTON = CL._button_by_attribute_xpath("type", "submit")
    USER_DROPDOWN_TAB = "//span[@class='oxd-userdropdown-tab']"
    LOGOUT_BUTTON = "//ul[@role='menu']//a[normalize-space()='Logout']"

    def __init__(self, page):
        super().__init__(page)
        self.page = page

    @staticmethod
    def SOCIAL_LINK(index: int):
        return f"//div[@class='orangehrm-login-footer-sm']/a[{index}]"

    def _go_to_orange_hrm_login(self):
        self._goto(self.URL)
        self.page.wait_for_load_state("load")

    def _login(self):
        self._perform_login()
        self._click_submit_button()

    def _perform_login(self, username: str = None, password: str = None):
        str_username = username or "Admin"
        str_password = password or "admin123"
        self._fill(self.USER_NAME_BUTTON, str_username)
        self._fill(self.PASSWORD_BUTTON, str_password)

    def _click_submit_button(self):
        self._click(self.SUBMIT_BUTTON)

    def _verify_dashboard_page(self):
        self._expect_to_have_url("/dashboard")

    def _logout(self):
        self._click(self.USER_DROPDOWN_TAB)
        self._wait_for_element(self.LOGOUT_BUTTON)
        self._click(self.LOGOUT_BUTTON)
        self._expect_to_have_url("/login")

    def _open_social_tab(self, index: int, keyword: str):
        new_page: Page =  self._open_new_tab(self.SOCIAL_LINK(index))
        url = new_page.url.lower()
        assert "orangehrm" in url, f"URL không khớp từ khóa OrangeHRM: {url}"
        assert f"{keyword}" in url, f"URL không khớp từ khóa '{keyword}': {url}"
        return new_page

    def _open_linkedin_tab(self):
        return self._open_social_tab(1, "linkedin")

    def _open_facebook_tab(self):
        return self._open_social_tab(2, "facebook")
        
    def _open_twitter_tab(self):
        new_page = self._open_social_tab(3, "x.com")
        return TwitterOrange(new_page)
            
    def _open_youtube_tab(self):
        return self._open_social_tab(4, "youtube")