from playwright.sync_api import expect

class SocialPage:

    def __init__(self, page):
        self.page = page

        self.icon_x = page.locator("//*[name()='path' and contains(@d,'M21.742 21')]")

        self.title_orangehrm = page.locator("(//span[@class='css-1jxf684 r-bcqeeo r-1ttztb7 r-qvutc0 r-poiln3'][normalize-space()='OrangeHRM'])[3]")

    def verify_twitter_page(self):
        expect(self.icon_x).to_be_visible()
        expect(self.title_orangehrm).to_have_text("OrangeHRM")
