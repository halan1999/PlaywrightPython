from playwright.sync_api import Page, expect

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

    def _select2(self, xpath_dropdown : str, item_choose : str):
        # Click to open dropdownlist
        self._click(xpath_dropdown)

        # Verify list item visible
        xpath_dropdown_menu = '//ul[contains(@class,"dropdown-menu")]'
        expect(self.page.locator(xpath_dropdown_menu)).to_be_visible()

        # Choose expected item
        xpath_item = f'//li[normalize-space()="{item_choose}"]'
        self._click(xpath_item)

    def _verify_visible(self, xpath_element : str):
        locator_element = self.page.locator(xpath_element)
        expect(locator_element).to_be_visible()

    def _take_screenshot(self, filename: str):
        path = f"screenshots/{filename}"
        self.page.screenshot(path=path)
        print(f"[SCREENSHOT] Lưu tại: {path}")