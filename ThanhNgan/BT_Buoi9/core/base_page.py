from playwright.sync_api import Page, expect, Locator, TimeoutError
from datetime import datetime
class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def _goto(self, url: str):
        print(f"Truy cập đến: {url}")
        self.page.goto(url, wait_until="domcontentloaded")

    def _get_locator(self, locator: str):
        return self.page.locator(locator)
    
    def _get_url(self) -> str:
        return self.page.url

    def _expect_to_be_visible(self, locator:str):
        try:
            expect(self.page.locator(locator)).to_be_visible(timeout=5000)
        except TimeoutError:
            print(f"Lỗi Element {locator} không hiển thị")
            self._take_screenshot(f"error_locator_visible_{locator}.png")
            raise

    def _get_text(self, locator: str) -> str:
        return self.page.locator(locator).inner_text()
        
    def _click(self, locator: str):
        try:
            element = self.page.locator(locator)
            element.wait_for(state = "visible", timeout=5000  )
            print(f"Click {locator}")
            element.click()
        except TimeoutError:
            print(f"Lỗi Element {locator} không hiển thị")
            print("element:",element)
            self._take_screenshot(f"error_click_{element}.png")
            raise

    def _fill(self, locator: str, text: str):
        print(f"Fill {text} vào {locator}")
        self._get_locator(locator).fill(text)

    def _assert_text_visible(self, locator: str, text: str):
        print(f"Assert Kiểm tra '{text}' hiển thị")
        expect(self._get_locator(locator)).to_contain_text(text)

    def _take_screenshot(self, filename: str):
        path = f"./BT_Buoi9/screenshots/{filename}_{datetime.now().date()}.png"
        self.page.screenshot(path=path)
        print(f"[SCREENSHOT] Lưu tại: {path}")

    def _click_to_open_new_tab(self,locator):
        with self.page.context.expect_page(timeout=30000) as new_page_info:
            self._click(locator) 
        new_page = new_page_info.value
        new_page.wait_for_load_state()
        return new_page

    def _back_to_main_page(self):
        self.page.bring_to_front()
        self.page.wait_for_load_state() 

    def _upload_file(self, locator: str, file_path: str):
        self.page.set_input_files(locator, file_path)
        print(f"Upload file successfully")
        self._take_screenshot("after_upload_file.png")

    def _get_input_value(self, locator: str) -> str:
        return self.page.locator(locator).input_value()
    
    

        
    
        