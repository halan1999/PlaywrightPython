from playwright.sync_api import Page, expect
from Core.config import NEW_TAB_URL
from pages.Multitab_demo.new_tab_windows_page import NewTabWindowsPage

def test_new_tab_windows(page:Page):
   p= NewTabWindowsPage(page, NEW_TAB_URL)
   p.open()
   p.assert_heading("Opening a new window")
   popup=p.open_new_tab()
   expect(popup).to_have_url("https://the-internet.herokuapp.com/windows/new")

    