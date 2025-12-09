from playwright.sync_api import Page, expect
class SocialPage:
    locator_map = {
        "Sign in to see who you already know at OrangeHRM":"#base-contextual-sign-in-modal-modal-header",
        "See more from OrangeHRM - World's Most Popular Opensource HRIS | Secaucus NJ":"//span[@class='x193iq5w xeuugli x13faqbe x1vvkbs x1xmvt09 x1lliihq x1s928wv xhkezso x1gmr53x x1cpjm7i x1fgarty x1943h6x xtoi2st x3x7a5m x1603h9y x1u7k74 x1xlr1w8 xzsf02u x2b8uid']",
        "OrangeHRM":"(//span[@class='css-1jxf684 r-bcqeeo r-1ttztb7 r-qvutc0 r-poiln3'][normalize-space()='OrangeHRM'])[1]",
        "OrangeHRM Inc":"//span[normalize-space()='OrangeHRM Inc']"
    }

    def __init__(self, page):
        self.page = page

    def verify_heading(self, text: str):
        locator = self.page.locator(self.locator_map[text])
        expect(locator).to_contain_text(text)

