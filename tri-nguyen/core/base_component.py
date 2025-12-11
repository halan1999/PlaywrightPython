from playwright.sync_api import expect, Page

class BaseHeaderComponent:
    def __init__(self, page: Page):
        self.page = page
        self.logo_header = page.locator("//div[@class='header-wrapper']//a[@href='https://hrm.anhtester.com/erp/desk']")
        self.account_setting = page.locator("//a[@data-original-title='Account Settings']")
        self.apps = page.locator("//span[@data-original-title='Apps']/parent::a")
        self.system_calendar = page.locator("//a[@data-original-title='System Calendar']")
        self.system_report = page.locator("//a[@data-original-title='System Reports']")
        self.language_icon = page.locator("//ul//li[1]//a[contains(@class, 'dropdown-toggle')]")
        self.todo_list = page.locator("//a[@data-original-title='Todo List']")
        # self.account_profile = page.locator("//header//a//img[@class='user-avtar']")
        