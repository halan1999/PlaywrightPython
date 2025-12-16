from playwright.sync_api import expect


class BasePage:
    def __init__(self, page):
        self.page = page

    def click(self, locator):
        self.page.locator(locator).click()

    def click_if_visible(self, locator):
        element = self.page.locator(locator)
        if element.is_visible():
            element.click()

    def fill(self, locator, value):
        self.page.locator(locator).fill(value)

    def is_visible(self, locator):
        return self.page.locator(locator).is_visible()

    def expect_visible(self, locator):
        expect(self.page.locator(locator)).to_be_visible()

    def bring_to_front(self):
        self.page.bring_to_front()
