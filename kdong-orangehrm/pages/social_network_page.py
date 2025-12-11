from core.base_page import BasePage
from playwright.sync_api import expect,Page, Locator
from pages.new_social_page import NewSocialPage

class SocialNetworkPage(BasePage):
    # Social Media Locators
    LINKEDIN_ICON_LINK = "//a[@href='https://www.linkedin.com/company/orangehrm/mycompany/']"
    FACEBOOK_ICON_LINK = "//a[@href='https://www.facebook.com/OrangeHRM/']"
    TWITTER_ICON_LINK = "a[href*='twitter.com/orangehrm']"
    YOUTUBE_ICON_LINK = "https://www.youtube.com/c/OrangeHRMInc"
    PAGE_TITLE = "OrangeHRM"

    def __init__(self, page: Page):
        super().__init__(page)
    
    def get_heading_text(self, heading) -> str:
        return self._get_text(f"//h1[contains(normalize-space(), '{heading}')]")

    def verify_element(self):
        expect(self.page.locator(self.icon_twitter)).to_be_visible()

    
    
    