from playwright.sync_api import  Page, expect
import re, time
def test_bai_tap1(page: Page):
    page.goto('https://voz.vn')
    expect(page).to_have_title(re.compile('VOZ'))
    print('Tieu de hop le')
    expect(page).to_have_url(re.compile('voz.vn'))
    print('URL hop le')
    time.sleep(10)