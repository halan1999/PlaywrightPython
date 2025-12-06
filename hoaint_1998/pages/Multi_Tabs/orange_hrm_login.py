from core.base_page import BasePage
from core.common_locators import CommonLocators
from playwright.sync_api import Page

class Orange_Hrm_Login(BasePage):
    URL = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"

    def __init__(self, page):
        super().__init__(page)
        self.page = page

    @staticmethod
    def SOCIAL_LINK(index: int):
        return f"//div[@class='orangehrm-login-footer-sm']/a[{index}]"

    def _go_to_orange_hrm_login(self):
        self._goto(self.URL)

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
        return self._open_social_tab(3, "x.com")
        
    def _open_youtube_tab(self):
        return self._open_social_tab(4, "youtube")