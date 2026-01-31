from BT_BUOI8.components.menu.menu_component import MenuComponent
from BT_BUOI8.core.base_page import BasePage
from playwright.sync_api import expect

class ManageClients(BasePage):
    ADD_NEW_BUTTON = "//a[normalize-space()='Add New']"

    def __init__(self, page):
        super().__init__(page)
        # Pin menu to current page
        self.menu = MenuComponent(page)

    def open_menu_button(self):
        self.menu.open_menu('Manage Clients')

    def assert_open_successful(self):
        expect(self.page).to_have_url("https://hrm.anhtester.com/erp/clients-list")
        self._take_screenshot("Open_menu_client_successful.png")

    def add_new_client(self):
        self._click(self.ADD_NEW_BUTTON, 'Add New Client Button')
        self._take_screenshot("Add_new_client_form.png")
