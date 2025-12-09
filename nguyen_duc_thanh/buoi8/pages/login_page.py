from buoi8.pages.base_page import BasePage
from buoi8.pages.multi_tab.facebook_page import FacebookPage
from buoi8.pages.multi_tab.linkedln_page import LinkedlnPage
from buoi8.pages.multi_tab.twitter_page import TwitterPage
from buoi8.pages.multi_tab.youtube_page import YoutubePage


class LoginPage(BasePage):

    URL = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    YOUTUBE_ICON = "//a[@href='https://www.youtube.com/c/OrangeHRMInc']"
    LINKEDLN_ICON = "//a[@href='https://www.linkedin.com/company/orangehrm/mycompany/']"
    FACEBOOK_ICON = "//a[@href='https://www.facebook.com/OrangeHRM/']"
    TWITTER_ICON = "//a[@href='https://twitter.com/orangehrm?lang=en']"
    H5 = "//h5[@class='oxd-text oxd-text--h5 orangehrm-login-title']"

    def __init__(self, page):
        super().__init__(page)


    def get_heading5(self):
        return self.get_text(self.H5)

    def go_to_loginpage(self):
        self.goto(self.URL)

    def open_youtube_tab(self) -> YoutubePage:
        
        with self.page.context.expect_page() as new_page_info:
            self.click_element(self.YOUTUBE_ICON)

        new_page = new_page_info.value
        new_page.wait_for_load_state()

        return YoutubePage(new_page)

    def open_facebook_tab(self) -> FacebookPage:
        with self.page.context.expect_page() as new_page_info:
            self.click_element(self.FACEBOOK_ICON)

        new_page = new_page_info.value
        new_page.wait_for_load_state()

        return FacebookPage(new_page)

    def open_linkedin_tab(self) -> LinkedlnPage:
        with self.page.context.expect_page() as new_page_info:
            self.click_element(self.LINKEDLN_ICON)

        new_page = new_page_info.value
        new_page.wait_for_load_state()

        return LinkedlnPage(new_page)

    def open_twitter_tab(self) -> TwitterPage:
        with self.page.context.expect_page() as new_page_info:
            self.click_element(self.TWITTER_ICON)

        new_page = new_page_info.value
        new_page.wait_for_load_state()

        return TwitterPage(new_page)
