from playwright.sync_api import Page, expect

class MultiWindowPage:
    def __init__(self, page: Page):
        self.page = page
        self.link_click_here = "a[href='/windows/new']"

    def open(self):
        self.page.goto("https://the-internet.herokuapp.com/windows")
        return self

    def click_here_and_open_new_tab(self):
        with self.page.context.expect_page() as new_page_event:
            self.page.click(self.link_click_here)
        return new_page_event.value
