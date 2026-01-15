import time
from buoi8.pages.base_page import BasePage


class YoutubePage(BasePage):
    def __init__(self, page):
        super().__init__(page)

    YOUTUBE_CHANNEL = "//span[normalize-space()='OrangeHRM Inc']"

    def assert_visible_youtube_channel(self):
        youtube_channel = self.get_text(self.YOUTUBE_CHANNEL)
        assert youtube_channel == "OrangeHRM Inc"
    
    