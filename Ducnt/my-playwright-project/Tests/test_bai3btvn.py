from playwright.sync_api import  Page, expect
import re, time

def test_crmanhtester (page: Page):
    page.goto('https://the-internet.herokuapp.com/tables')