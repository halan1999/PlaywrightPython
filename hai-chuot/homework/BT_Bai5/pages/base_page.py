from playwright.sync_api import Page, expect

class BasePage:
    Xpath_header_homepage = '//div[@class="primary_header"]//div[@class="app_logo"]'
    Xpath_btn_expand_menu = '//button[@id="react-burger-menu-btn"]'
    Xpath_cart = '//div[@id="shopping_cart_container"]//a'

    def __init__(self, page : Page):
        self.page = page
    
    def _click_expand_menu(self, label_menu : str):
        self.page.locator(self.Xpath_btn_expand_menu).click()

        xpath_sub_menu = f'//a[normalize-space()="{label_menu}"]'
        self.page.locator(xpath_sub_menu).click()

    def _click_cart_button(self):
        self.page.locator(self.Xpath_cart).click()
    
    def _verify_home_page_visible(self):
        expect(self.page.locator(self.Xpath_header_homepage)).to_be_visible()