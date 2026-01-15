from buoi7.components.header_component import HeaderComponent

def test_run_flow_header(page,logged_page):
    header = HeaderComponent(page)
    header.click_to_headers()
