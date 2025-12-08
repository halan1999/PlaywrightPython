from playwright.sync_api import Page, expect

class BasePage:
    def __init__(self, page: Page):
        self.page=page
    def goto(self, url: str) -> None:
        self.page.goto(url)
    def fill(self, locator: str, text: str) -> None:
        self.page.locator(locator).fill(text)
    def click(self, locator: str) -> None:
        self.page.locator(locator).click()
    def should_visible(self, locator: str) -> None:
        loc=self.page.locator(locator)
        expect(loc.first).to_be_visible()
    def get_text(self, locator: str) ->str:
        return self.page.locator(locator).inner_text()
    def take_full_page_screenshot(self, path: str) ->None:
        self.page.screenshot(path=path, full_page=True)
    def take_element_screenshot(self, locator: str, path:str) -> None:
        self.page.locator(locator).screenshot(path=path)
        

    