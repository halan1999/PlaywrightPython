from components.header_components import HeaderComponent
from playwright.sync_api import expect, Page, sync_playwright
import time, re
import json

def test_loggout_successfully(perform_login, page):
    #logout
        logout = HeaderComponent(page)
        logout.test_loggout()
        time.sleep(5)