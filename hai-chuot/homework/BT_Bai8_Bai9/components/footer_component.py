from enum import Enum
from playwright.sync_api import Page
from core.base_page import BasePage

class LinkFooter(Enum):
    """
    Links to related pages in the footer
    """
    LINKEDIN = 'https://www.linkedin.com/company/orangehrm/mycompany/'    
    FACEBOOK = 'https://www.facebook.com/OrangeHRM/'
    TWITTER = 'https://twitter.com/orangehrm?lang=en'
    YOUTUBE = 'https://www.youtube.com/c/OrangeHRMInc'

class FooterComponent(BasePage):    
    def open_related_page(self, link_footer: LinkFooter) -> Page:
        xpath_icon = f'//a[@href="{link_footer.value}"]'

        with self.page.context.expect_page() as new_page:
            self._click(xpath_icon)

        opened_page = new_page.value
        opened_page.wait_for_load_state()

        return opened_page