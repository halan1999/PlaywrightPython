from playwright.sync_api import Page, expect, Locator
from typing import Self
import re
from pathlib import Path

class BasePage():
    def __init__(self, page: Page):
        self.page = page

    #--------------------------
    #region BASIC ACTION -------
    #--------------------------

    def _get_locator(self, locator: str):
        return self.page.locator(locator)

    def _goto(self, url: str) :
        return self.page.goto(url, wait_until="domcontentloaded")
        
    
    def _click(self, locator: str | Locator):
        loc : Locator = locator if isinstance(locator, Locator) else self._get_locator(locator)
        loc.click()
        
    
    def _dbclick(self, locator: str):
        return self.page.locator(locator).dblclick()
    
    def _fill(self, locator: str | Locator, value: str):
        loc : Locator = locator if isinstance(locator, Locator) else self._get_locator(locator)
        loc.fill(value)
        # return self.page.locator(locator).fill(value)
    
    def _inner_text(self, locator: str):
        """
        Lấy giá trị text hiển thị trên màn hình của locator
        """
        return self._get_locator(locator).inner_text().strip()
    
    def _select_option(self, locator: str, value=None):
        selector = self._get_locator(locator)

        if isinstance(value, list):
            selector.select_option(value)
            return
        selector.select_option(value)
    
    # endregion
    
    #--------------------------
    # region Page
    #--------------------------
    def _bring_to_font(self):
        """
        trở về trang mà mình muốn
        """
        self.page.bring_to_front()

    def _open_new_tab(self, locator: str, timeout=15000):
        """
        Thực hiện mở mới tab thông qua action click
        """
        with self.page.context.expect_page(timeout=timeout) as new_page_info:
            self._click(locator)
        new_page = new_page_info.value
        new_page.wait_for_load_state("domcontentloaded")
        return new_page
    
    # endregion
    
    #--------------------------
    # region LocatorAssertions = check the condition
    #--------------------------
    def _expect_to_have_url(self, url: str):
        return expect(self.page).to_have_url(re.compile(f".*{url}.*"))
      
    
    def _expect_to_be_visible(self, locator: str, message: str = None):
        """
        check whether an element is visible in the browser's viewport 
        """
        try:
            expect(self._get_locator(locator)).to_be_visible()
        except Exception:
            raise AssertionError(message or f"{locator} is not visible")
        
    
    def _expect_to_be_hidden(self, locator: str, message: str = None):
        """
        check if element is hidden
        """
        try:
            expect(self._get_locator(locator)).to_be_hidden()
        except Exception:
            raise AssertionError(message or f"{locator} is not hidden")
        
    
    def _expect_to_be_disabled(self, locator: str, message: str = None):
        """
        check whether an element is disabled (not interactable)
        """
        try:
            expect(self._get_locator(locator)).to_be_disabled()
        except Exception:
            raise AssertionError(message or f"{locator} is not disabled")
        
    
    def _expect_to_be_enabled(self, locator: str, message: str = None):
        """
        check whether an element is enable (interactable)
        """
        try:
            expect(self._get_locator(locator)).to_be_enabled()
        except Exception:
            raise AssertionError(message or f"{locator} is not enabled")
    # endregion    
    #--------------------------
    # region Wait
    #--------------------------
    def _wait_for_element(self, locator: str, timeout: int = 30000):
        return self.page.locator(locator).wait_for(state="visible", timeout=timeout)
        
    # endregion
    
    #--------------------------
    #------ TAKE A SCREENSHOT -------
    #--------------------------
    def _take_screenshot(self, filename: str):
        file_path = Path(f"screenshots/{filename}.png")
        self.page.screenshot(path=file_path)
        print(f"[SCREENSHOT] Lưu tại: {file_path}")
