from playwright.sync_api import Page

class BasePage:
    def __init__(self, page: Page):
        self.page = page
    
    def goto(self,url):
        self.page.goto(url)

    def get_locator(self,locator):
        return self.page.locator(locator)

    def send_text(self, locator, text):
        self.get_locator(locator).fill(text)
        
    def click_element(self,locator):
        try:
            self.get_locator(locator).click()
        except TimeoutError:
            print(f"Cannot click in {locator}")
            raise
    
    def take_screenshot(self, filename: str):
        path = f"buoi6/hrm/screenshots/{filename}"
        self.page.screenshot(path=path)
        print(f"[SCREENSHOT] Lưu tại: {path}")

