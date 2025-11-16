from components.header_components import HeaderComponent
from playwright.sync_api import expect, sync_playwright
import json, re, time

def test_click_icon_header(perform_login, page):
    # click on icon logo
        click_header_icon = HeaderComponent(page)
        click_header_icon.test_click_icon_logo_header()
    # click on account setting
        click_header_icon.test_click_icon_account_setting()
    # click on icon app
        click_header_icon.test_click_icon_apps()
    # click on icon system calendar
        click_header_icon.test_click_icon_system_calendar()
    # click on icon system report
        click_header_icon.test_click_icon_system_report()
    # click on icon language
        click_header_icon.test_click_language_icon()
    # click on todo list icon
        click_header_icon.test_click_todo_list()