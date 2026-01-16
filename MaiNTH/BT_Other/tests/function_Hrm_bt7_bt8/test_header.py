import pytest
from playwright.sync_api import Page, expect
from pages.login_page import LoginPage
from components.header_component import Header_component

@pytest.mark.usefixtures("logged_in_class")
class TestHeader():
    def test_Header(self):
        print("[DEBUG TEST] type of self.page:", type(self.page))
        header = Header_component(self.page)
        # Click từng item trên header
        header.click_all_header_items()
        # Click button Logout
        header.log_out()

