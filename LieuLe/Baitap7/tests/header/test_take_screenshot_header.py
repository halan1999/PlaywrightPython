def test_capture_all(dashboard):
    dashboard.page.wait_for_url("**/erp/desk")
    dashboard.header.capture_all()
    

