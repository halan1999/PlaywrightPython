from playwright.sync_api import Page, expect, Locator, TimeoutError

class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def _goto(self, url: str):
        print(f"Truy cập đến: {url}")
        self.page.goto(url)

    def _get_locator(self, locator: str):
        return self.page.locator(locator)
    
    def _click(self, locator: str):
        try:
            print(f"Click {locator}")
            self._get_locator(locator).click()
        except TimeoutError:
            print(f"Lỗi không thể click vào {locator}")
            raise
    
    def _fill(self, locator: str, text: str):
        print(f"Fill {text} vào {locator}")
        self._get_locator(locator).fill(text)

    def _assert_text_visible(self, locator: str, text: str):
        print(f"Assert Kiểm tra '{text}' hiển thị")
        expect(self._get_locator(locator)).to_contain_text(text)

    

        
    
        