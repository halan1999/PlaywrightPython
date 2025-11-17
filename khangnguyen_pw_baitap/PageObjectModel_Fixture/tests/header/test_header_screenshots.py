from components.header_component import HeaderComponent

def test_header_screenshot(logged_in_page):
    header = HeaderComponent(logged_in_page)
    header.click_header_items_and_take_screenshot()
    print('Took screenshots for all header items!')