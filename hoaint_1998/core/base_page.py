from playwright.sync_api import Page, expect
from typing import Self
import re
from pathlib import Path

class BasePage():
    def __init__(self, page: Page):
        self.page = page

    #--------------------------
    #------ BASIC ACTION -------
    #--------------------------

    def _get_locator(self, locator: str):
        return self.page.locator(locator)

    def _goto(self, url: str) :
        return self.page.goto(url, wait_until="domcontentloaded")
        
    
    def _click(self, locator: str):
        return self.page.locator(locator).click()
        
    
    def _dbclick(self, locator: str):
        return self.page.locator(locator).dblclick()
    
    def _fill(self, locator: str, value: str):
        return self.page.locator(locator).fill(value)
    
    #--------------------------
    #------ LocatorAssertions = check the condition -------
    #--------------------------
    def _expect_to_have_url(self, url: str):
        return expect(self.page).to_have_url(re.compile(f".*{url}$"))
      
    
    def _expect_to_be_visible(self, locator: str):
        """
        check whether an element is visible in the browser's viewport 
        """
        return expect(self.page.locator(locator)).to_be_visible()
        
    
    def _expect_to_be_hidden(self, locator: str):
        """
        check if element is hidden
        """
        return expect(self.page.locator(locator)).to_be_hidden()
        
    
    def _expect_to_be_disabled(self, locator: str):
        """
        check whether an element is disabled (not interactable)
        """
        return expect(self.page.locator(locator)).to_be_disabled()
        
    
    def _expect_to_be_enabled(self, locator: str):
        """
        check whether an element is enable (interactable)
        """
        return expect(self.page.locator(locator)).to_be_enabled()
        
    
    #--------------------------
    #------ WAIT -------
    #--------------------------
    def _wait_for_element(self, locator: str, timeout: int = 30000):
        return self.page.locator(locator).wait_for(state="visible", timeout=timeout)
        
    
    #--------------------------
    #------ TAKE A SCREENSHOT -------
    #--------------------------
    def _take_screenshot(self, filename: str):
        file_path = Path(f"screenshots/{filename}.png")
        self.page.screenshot(path=file_path)
        print(f"[SCREENSHOT] Lưu tại: {file_path}")
