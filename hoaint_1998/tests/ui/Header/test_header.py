from components.header_components import HeaderComponents

def test_run_flow_header(logined_page, page):
    header = HeaderComponents(page)
    header._click_and_take_screenshot_all_button_in_header()