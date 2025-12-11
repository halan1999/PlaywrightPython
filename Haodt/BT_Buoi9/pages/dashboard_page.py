from playwright.sync_api import expect

class DashboardPage:

    def __init__(self, page):
        self.page = page
        self.dashboard_header = page.locator("//h6[normalize-space()='Dashboard']")  # Dashboard

        self.user_menu = page.locator("//span[@class='oxd-userdropdown-tab']")
        self.logout_btn = page.locator("//a[normalize-space()='Logout']")

    def verify_dashboard(self):
        expect(self.dashboard_header).to_have_text("Dashboard")

    def logout(self):
        self.user_menu.click()
        self.logout_btn.click()
