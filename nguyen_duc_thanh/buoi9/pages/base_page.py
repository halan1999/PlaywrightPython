import json
import os
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
    
    def get_url(self):
        return self.page.url


    def get_text(self, locator):
        el = self.get_locator(locator)
        el.wait_for(state="visible")   
        text = el.text_content()
        return text.strip() if text else None

    def get_credential(self):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(current_dir, "../data/credentials.json")
        with open(file_path) as f:
            return json.load(f)
        
    def _bring_to_front(self):
        self.page.bring_to_front()