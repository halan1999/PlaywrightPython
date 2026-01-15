import allure
from playwright.sync_api import Page

class BasePage:
    def __init__(self, page : Page):
        self.page = page

    def _goToURL(self, url : str):
        self.page.goto(url, wait_until = 'domcontentloaded')

    def _click(self, xpath : str):
        locator = self.page.locator(xpath)
        locator.click()

    def _setText(self, xpath : str, input_data : str):
        locator = self.page.locator(xpath)
        locator.fill(input_data)

    def _take_screenshot(self, filename: str, name : str):
        path = f"screenshots/{filename}"
        image = self.page.screenshot(path = path, full_page = True)
        allure.attach(image, name = name, attachment_type = allure.attachment_type.PNG)        
        print(f"[SCREENSHOT] Lưu tại: {path}")