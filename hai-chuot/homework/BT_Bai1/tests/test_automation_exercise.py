from playwright.sync_api import Page, expect
import re

def test_homepage_automationexercise(page: Page):
    url_test = "https://www.automationexercise.com/"
    
    page.goto(url_test)

    expect(page).to_have_title(re.compile("Automation Exercise"))
    
    expect(page).to_have_url(url_test)