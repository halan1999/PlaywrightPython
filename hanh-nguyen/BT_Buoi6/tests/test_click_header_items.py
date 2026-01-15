from components.header_component import HeaderComponent
from playwright.sync_api import Playwright

def test_click_header_items(page):
    header = HeaderComponent(page)

    header.click_logo()
    header._take_screenshot('screenshots/header_logo.png')

    header.click_account_setting()
    header._take_screenshot('screenshots/account_settings.png')

    header.click_app_settings()
    header._take_screenshot('screenshots/apps.png')

    header.click_system_calendar()
    header._take_screenshot('screenshots/system_calendar.png')

    header.click_system_report()
    header._take_screenshot('screenshots/system_reports.png')

    header.click_country_selector()
    header._take_screenshot('screenshots/country_selector.png')

    header.click_todo_list()
    header._take_screenshot('screenshots/todo_lists.png')

    header.click_user_account()
    header._take_screenshot('screenshots/user_accounts.png')
