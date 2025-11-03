from playwright.sync_api import Page, expect
from typing import Self
import re

class BasePage():
    def __init__(self, page: Page):
        self.page = page

    #--------------------------
    #------ BASIC ACTION -------
    #--------------------------

    def _get_locator(self, locator: str) -> Self:
        self.page.locator(locator)
        return self

    def _goto(self, url: str) -> Self:
        self.page.goto(url, wait_until="domcontentloaded")
        return self
    
    def _click(self, locator: str) -> Self:
        self.page.locator(locator).click()
        return self
    
    def _dbclick(self, locator: str) -> Self:
        self.page.locator(locator).dblclick()
        return self
    
    def _fill(self, locator: str, value: str) -> Self:
        self.page.locator(locator).fill(value)
        return self
    
    #--------------------------
    #------ LocatorAssertions = check the condition -------
    #--------------------------
    def _expect_to_have_url(self, url: str) -> Self:
        expect(self.page).to_have_url(re.compile(f".*{url}$"))
        return self
    
    def _expect_to_be_visible(self, locator: str) -> Self:
        """
        check whether an element is visible in the browser's viewport 
        """
        expect(self.page.locator(locator)).to_be_visible()
        return self
    
    def _expect_to_be_hidden(self, locator: str) -> Self:
        """
        check if element is hidden
        """
        expect(self.page.locator(locator)).to_be_hidden()
        return self
    
    def _expect_to_be_disabled(self, locator: str) -> Self:
        """
        check whether an element is disabled (not interactable)
        """
        expect(self.page.locator(locator)).to_be_disabled()
        return self
    
    def _expect_to_be_enabled(self, locator: str) -> Self:
        """
        check whether an element is enable (interactable)
        """
        expect(self.page.locator(locator)).to_be_enabled()
        return self 
    
    #--------------------------
    #------ WAIT -------
    #--------------------------
    def _wait_for_element(self, locator: str, timeout: int = 30000) -> Self:
        self.page.locator(locator).wait_for(state="visible", timeout=timeout)
        return self
