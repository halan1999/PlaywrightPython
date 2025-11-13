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

    def _click_menu(self, main_menu : str):
        xpath_main_menu = f'//a[normalize-space()="{main_menu}"]'
        self.page.locator(xpath_main_menu).click()

    def _click_menu(self, main_menu : str, sub_menu : str):
        xpath_main_menu = f'//a[normalize-space()="{main_menu}"]'
        xpath_sub_menu = f'{xpath_main_menu}/following-sibling::ul//a[normalize-space()="{sub_menu}"]'
        self.page.locator(xpath_main_menu).click()
        self.page.locator(xpath_sub_menu).click()

    def _take_screenshot(self, filename: str):
        path = f"screenshots/{filename}"
        self.page.screenshot(path=path)
        print(f"[SCREENSHOT] Lưu tại: {path}")