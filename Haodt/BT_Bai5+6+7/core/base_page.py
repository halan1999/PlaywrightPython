from playwright.sync_api import Page, expect, Locator, TimeoutError
import time
class BasePage:

    def __init__(self,page:Page):
        self.page=page
    
    def _open_url(self,url:str):
        print (f"[BasePage] Navigate to: {url}")
        self.page.goto(url, wait_until="domcontentloaded")

    def _get_locator(self, locator:str) -> Locator:
        return self.page.locator(locator)
    
    def _click(self,locator:str):
        try:
            self._get_locator(locator).click()
        except TimeoutError:
            print(f"Error: Can't click to {locator}")
            raise

    def _fill(self,locator:str,text:str):
        print (f"[Fill] '{text}' into {locator}")
        self._get_locator(locator).fill(text)

    def _assert_text_visible(self,locator:str,value:str):
        print(f"[Assert] Verify '{value}' is displayed")
        expect(self._get_locator(locator)).to_contain_text(value)

    def _select_menu(self,texts:str):
        Locator="//li//a//span[normalize-space()={text}]"

    def _take_screenshot(self,filename:str):
        path = f"screenshots/{filename}_{int(time.time())}.png"
        self.page.screenshot(path=path)
        print(f"[SCREENSHOT] save as: {path}")

    

    

        