from Core.Base_page import BasePage
class DashboardPage(BasePage):
    breadcrumb_dashboard="//li[contains(@class,'breadcrumb-item') and normalize-space()='Dashboard']"
    def is_loaded(self):
        return self.is_visible(self.breadcrumb_dashboard)
    