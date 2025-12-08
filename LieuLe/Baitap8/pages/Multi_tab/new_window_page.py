from playwright.sync_api import Page, expect

class NewWindowPage:
    def __init__(self, page: Page):
        self.page = page

    def verify_new_window(self):
        self.page.bring_to_front()
        expect(self.page.locator("h3")).to_have_text("New Window")
        print("✔ Verified: New Window")
