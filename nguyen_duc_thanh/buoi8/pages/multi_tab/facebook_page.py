import time
from buoi8.pages.base_page import BasePage


class FacebookPage(BasePage):
    
    def __init__(self, page):
        super().__init__(page)
    
    FACEBOOK_NAME = "//span[contains(text(),'OrangeHRM is the world’s friendliest HR management')]"
    CLOSE_BUTTON = "//div[@aria-label='Close']"

    def assert_visible_facebook_url(self):
        self.click_element(self.CLOSE_BUTTON)
        time.sleep(3)
        facebook_name = self.get_text(self.FACEBOOK_NAME)
        facebook_name = self.get_url()
        print(facebook_name)
        assert facebook_name == "https://www.facebook.com/OrangeHRM/"
