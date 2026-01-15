from playwright.sync_api import Page, expect
from playwright.sync_api import sync_playwright
import time, re
import sys
import pytest

# Dashboard
# //input[@id='search_input']
# //div[contains(@class , 'screen-options-btn') and contains(., 'Dashboard Options')] 
# //label[@for = 'widget_option_todos']
# //a[normalize-space(text()) = 'Reset Dashboard']
# //span[normalize-space(text()) = 'Invoices Awaiting Payment']
# //a[contains(.,'Sent') and contains(@href, 'status=4')]
# //a[contains(.,'My Tasks')]//i[@class= 'fa fa-tasks menu-icon']
# 