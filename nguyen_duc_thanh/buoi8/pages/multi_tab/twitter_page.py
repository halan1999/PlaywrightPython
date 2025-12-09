from buoi8.pages.base_page import BasePage


class TwitterPage(BasePage):

    def __init__(self, page):
        super().__init__(page)

    TWITTER_NAME = "//span[@class='css-1jxf684 r-bcqeeo r-1ttztb7 r-qvutc0 r-poiln3 r-b88u0q r-1awozwy r-6koalj r-1udh08x r-3s2u2q']" \
    "//span[@class='css-1jxf684 r-bcqeeo r-1ttztb7 r-qvutc0 r-poiln3'][normalize-space()='OrangeHRM']"

    
    def assert_visible_twitter(self):
        twitter = self.get_text(self.TWITTER_NAME)
        assert twitter == "OrangeHRM"
    