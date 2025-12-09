from playwright.sync_api import Page, expect
from pages.Multi_tab.multi_window_page import MultiWindowPage
from pages.Multi_tab.new_window_page import NewWindowPage

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.main_tab = page
        self.footer_icons = {
            "linkedin": {
                "selector": "a[href*='linkedin']",
                "expected": "LinkedIn"
            },
            "facebook": {
                "selector": "a[href*='facebook']",
                "expected": "Facebook"
            },
            "twitter": {
                "selector": "a[href*='twitter']",
                "expected": "X"    # twitter đổi thành X
            },
            "youtube": {
                "selector": "a[href*='youtube']",
                "expected": "YouTube"
            },
        }
        self.opened_tabs = {}


    def open(self):
        self.page.goto("https://opensource-demo.orangehrmlive.com/")
        return self

    def process_all_tabs_and_click_here(self):
        self._open_all_footer_tabs()
        self._process_click_here_window()

    def _open_all_social_tabs(self):
        for name, info in self.footer_icons.items():
            selector = info["selector"]
            new_page = self._open_new_tab(selector)
            self.opened_tabs[name] = new_page
            new_page.bring_to_front()
            self._verify_heading(new_page, info["expected"])
            self.main_tab.bring_to_front()
            print(f"↩ Back to Login tab after verify heading in: {name}")
    
    def _open_new_tab(self, selector):
        with self.page.context.expect_page() as event:
            self.page.click(selector)
        new_page = event.value
        new_page.wait_for_load_state("domcontentloaded")
        return new_page
    
    
    def get_tab(self, name: str) -> Page:
        return self.opened_tabs.get(name, None)

    def _verify_heading(self, page, expected=None):
        page.bring_to_front()
        text = None  
        heading_locator = page.locator("h1, h2")
        if heading_locator.count() > 0:
            text = heading_locator.first.inner_text().strip()
        if text:
            print(f"✔ Heading OK: {text}")
            return text

        title = page.title().strip()
        if title:
            print(f"✔ Title OK: {title}")
        return title

        meta_title = page.locator("meta[property='og:title']").get_attribute("content")
        if meta_title:
            meta_title = meta_title.strip()
            print(f"✔ Meta Title OK: {meta_title}")
            return meta_title
        if expected and expected.lower() in ["linkedin", "facebook", "twitter", "x", "youtube"]:
            assert expected.lower() in page.url.lower(), f"❌ URL mismatch: expected '{expected}' but got '{page.url}'"
            print(f"✔ URL OK: {page.url}")
            return page.url
        raise AssertionError(f"❌ Can not find heading/title in: {page.url}")

    def _process_click_here_window(self):
        multi = MultiWindowPage(self.page)
        multi.open()
        new_tab = multi.click_here_and_open_new_tab()

        new_window = NewWindowPage(new_tab)
        new_window.verify_new_window()

    def list_tabs(self):
        return list(self.opened_tabs.keys())