from playwright.sync_api import expect
from LieuLe.Baitap8_9.utils.json_reader import read_json

TWITTER_ICON = "//a[contains(@href,'twitter.com/orangehrm')]"
X_ICON = "//a[@aria-label='X'] | //svg[@aria-label='X']"
ORANGEHRM_TEXT = "//*[@data-testid='UserName']//span[text()='OrangeHRM']"

class LoginFooterComponent:
    def __init__(self, page):
        self.page = page
        self.context = page.context

    def open_social_tabs(self):
        expected_urls = read_json("data/social_links.json")
        tabs = {}

        for name in expected_urls.keys():
            locator = f"xpath=//a[contains(@href,'{name}')]"

            self.page.locator(locator).scroll_into_view_if_needed()

            with self.context.expect_page() as new_tab:
                self.page.click(locator)

            tab = new_tab.value
            tab.wait_for_load_state()

            print(f"✅ Opened {name}: {tab.url}")
            tabs[name] = tab

        return tabs

    def verify_social_tabs(self, tabs):
        expected_urls = read_json("data/social_links.json")

        for name, tab in tabs.items():
            print(f"🔍 Verifying {name}: {tab.url}")
            expect(tab).to_have_url(expected_urls[name])
            tab.close()

    def open_twitter_tab(self):
        # 1️⃣ Scroll all page TRANG → trigger footer render
        self.page.evaluate("window.scrollTo(0, document.body.scrollHeight)")

        # 2️⃣ Waiting footer icon in DOM
        twitter_icon = self.page.wait_for_selector(
            TWITTER_ICON,
            state="visible",
            timeout=10000
        )

        # 3️⃣ Click và get new tab 
        with self.page.context.expect_page() as new_page_event:
            twitter_icon.click()

        twitter_page = new_page_event.value
        twitter_page.wait_for_load_state("domcontentloaded")
        return twitter_page

    def verify_twitter_page(self, twitter_page):
        # 1️⃣ Verify icon X (Twitter)
        expect(twitter_page.locator(X_ICON)).to_be_visible()
    
        # 2️⃣ Verify OrangeHRM text under avatar
        expect(twitter_page.locator(ORANGEHRM_TEXT)).to_have_text("OrangeHRM")

    def back_to_login_tab(self):
        self.page.bring_to_front()