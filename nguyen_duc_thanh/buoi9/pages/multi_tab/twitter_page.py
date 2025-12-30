import time
from buoi9.pages.base_page import BasePage
from playwright.sync_api import expect

class TwitterPage(BasePage):

    def __init__(self, page):
        super().__init__(page)

    TWITTER_NAME = "//span[@class='css-1jxf684 r-bcqeeo r-1ttztb7 r-qvutc0 r-poiln3']" \
    "//span[@class='css-1jxf684 r-bcqeeo r-1ttztb7 r-qvutc0 r-poiln3'][normalize-space()='OrangeHRM']"
    TWITTER_ICON = "//a[@aria-label='X']"
    
    def assert_visible_twitter(self):
        time.sleep(3)
        visible = self.get_locator(self.TWITTER_ICON).is_visible()
        assert visible is True
        twitter = self.get_text(self.TWITTER_NAME)
        assert twitter == "OrangeHRM"


    
    