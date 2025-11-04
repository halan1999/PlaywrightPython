from pages.base_page import BasePage
from playwright.sync_api import expect

class menu_icon(BasePage):
    title_left_menu = "//li//label[normalize-space()='Your Apps'"
    